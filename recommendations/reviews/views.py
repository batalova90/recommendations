from datetime import datetime as dt

from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.views.decorators.cache import cache_page

from cloudinary.forms import cl_init_js_callbacks

from .models import Reviews, Categories, Genres, Creations, Authors, User, Comment, RaitingReview
from .forms import ReviewForm, CommentForm, CreationForm, RaitingReviewForm, SearchForm


def get_page(request, paginator):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    return paginator.get_page(page_number)


@cache_page(60 * 5)
def index(request):
    latest = Reviews.objects.all()
    paginator = Paginator(latest, 8) # убрать потом посты в settings
    page = get_page(request, paginator)
    return render(request, 'reviews/index.html', {'page': page, 'view': False})


@login_required()
def new_review(request):
    if request.method != 'POST':
        creation_formset = CreationForm(prefix='creation')
        review_formset = ReviewForm(prefix='review')
        return render(request, 'reviews/new.html',
                {'creation_form': creation_formset,
                 'review_form': review_formset,
                 'operation': 'Добавить обзор',
                 'add_or_save': 'Добавить',
                 'reviews': False})
    creation_formset = CreationForm(request.POST,
                                    prefix='creation')
    review_formset = ReviewForm(request.POST,
                                files=request.FILES,
                                prefix='review')
    print(creation_formset, '\n\n')
    print(review_formset, '\n\n', 'review')
    print(request.POST)
    if creation_formset.is_valid() and review_formset.is_valid():
        new_review = review_formset.save(commit=False)
        try:
            creation = Creations.objects.get(name=creation_formset.cleaned_data.get('name'),
                                             category__id=creation_formset.cleaned_data.get('category').id)
            new_review.creation = creation
            print('есть произведение')
        except ObjectDoesNotExist:
            print('нет произведения')
            new_creation = creation_formset.save()
            new_review.creation = new_creation
        author, created = Authors.objects.get_or_create(author=request.user)
        new_review.author = author
        new_review.save()
        return redirect(profile, request.user.username)
    return render(request, 'reviews/new.html',
                  {'creation_form': creation_formset,
                   'review_form': review_formset,
                   'operation': 'Добавить обзор',
                   'add_or_save': 'Добавить',
                   'reviews': False})


def review_view(request, username, review_id):
    review = get_object_or_404(Reviews,
                               author__author__username=username,
                               id=review_id)
    count = review.author.reviews.count
    form = CommentForm(request.POST)
    comments = Comment.objects.filter(review__id=review_id)
    scores = review.raiting_add.all()
    raiting = scores.aggregate(Avg('raiting')).get('raiting__avg')
    try:
        rating_author = review.author.sum_of_rating / review.author.number_of_rating
        review.author.rating = rating_author
        review.author.save()
    except ZeroDivisionError:
        rating_author = 0
    return render(request, 'reviews/review.html',
                  {'author': review.author.author,
                   'review': review,
                   'creation_name': review.creation.name,
                   'raiting': raiting,
                   'count_scores': scores.count,
                   'form': form,
                   'comments': comments,
                   'rating_author': rating_author,
                   'view': True,})


@login_required()
def review_edit(request, username, review_id):
    review = get_object_or_404(Reviews, id=review_id,
                               author__author__username=username)
    if request.user != review.author.author and not request.user.is_staff:
        return redirect(review_view, username, review_id)
    creation = Creations.objects.get(id=review.creation.id)
    if request.method != 'POST':
        creation_form = CreationForm(instance=creation, prefix='creation')
        review_form = ReviewForm(instance=review, prefix='review')
        return render(request, 'reviews/new.html',
                      {'creation_form': creation_form,
                       'review_form': review_form,
                       'operation': 'Редактировать запись',
                       'add_or_save': 'Cохранить',
                       'reviews': True,
                       'author': username,
                       'review_id': review_id})
    review_form = ReviewForm(request.POST or None,
                             files=request.FILES or None,
                             instance=review,
                             prefix='review')
    creation_form = CreationForm(request.POST or None,
                                 files=request.FILES or None,
                                 instance=creation,
                                 prefix='creation')
    if review_form.is_valid() and creation_form.is_valid():
        #creation = creation_form.save()
        review = review_form.save(commit=False)
        review.pub_date = dt.today()
        review.save()
        return redirect(review_view, username, review_id)
    return render(request, 'reviews/new.html',
                  {'creation_form': creation_form,
                   'review_form': review_form,
                   'operation': 'Редактировать запись',
                   'add_or_save': 'Сохранить',
                   'reviews': True})


def profile(request, username):
    author = get_object_or_404(Authors, author__username=username)
    reviews = author.reviews.all()
    rating_author = 0
    try:
        rating_author = author.sum_of_rating / author.number_of_rating
        author.rating = rating_author
        author.save()
    except ZeroDivisionError:
        raiting_author = 0
    if len(reviews) != 0:
        paginator = Paginator(reviews, 8)
        page = get_page(request, paginator)
        return render(request, 'reviews/profile.html',
                      {'author': username, 'page': page,
                       'count':  reviews.count,
                       'rating_author': rating_author,})
    return redirect('index')


def add_comment(request, username, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    if request.method != 'POST':
        form = CommentForm()
        return render(request,
                      'reviews/comments.html',
                      {'form': form, })
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.author = request.user
        comment.save()
        return redirect(review_view, username, review_id)
    return render(request,
                  'reviews/comments.html',
                  {'form': form,})


def creation(request, slug='1'):
    creation = get_object_or_404(Creations, slug=slug)
    reviews = creation.reviews.all()
    paginator = Paginator(reviews, 10)
    page = get_page(request, paginator)
    return render(request, 'reviews/creation.html', 
                  {'creation': creation, 'page': page})


@login_required()
def add_review_raiting(request, username, review_id):
    if 'raiting' in  request.GET:
        author = get_object_or_404(Authors,
                                   author__username=username)
        #клю ревью не проверен на существование
        review = author.reviews.get(id=review_id)
        if author.author == request.user:
            return redirect(review_view, username, review_id)
        score = request.GET['raiting']
        try:
            raiting_review, created = RaitingReview.objects.get_or_create(user=request.user,
                                                                          review=review,
                                                                          raiting=score)
        except IntegrityError:
            return redirect(review_view, username, review_id)

        if created:
            raiting_review.save()
            author.sum_of_rating += int(score)
            author.number_of_rating += 1
            author.rating = author.sum_of_rating / author.number_of_rating
            author.rating = round(author.rating, 3)
            author.save()
        return redirect(review_view, username, review_id)
    return redirect(review_view, username, review_id)


def review_search(request):
    form = SearchForm()
    query = ''
    total = 0
    result = ''
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Reviews.objects.filter(search_vector=query).all()
            total = result.count 
    return render(request, 'reviews/search.html',
                  {'form': form,
                   'query': query,
                   'result': result,
                   'total':total})



def top_authors(request):
    authors = Authors.objects.order_by('-rating')[:10].all()
    return render(request, 'reviews/top_authors.html',
                  {'authors': authors,})


# обработка 404 и 500
def page_not_found(request, exception):
    return render(request, 'misc/404.html',
                  {'path': request.path},
                  status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
