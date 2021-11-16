from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.forms import formset_factory

from .models import Reviews, Categories, Genres, Creations, Authors, User
from .forms import ReviewForm, CommentForm, CreationForm


def get_page(request, paginator):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    return paginator.get_page(page_number)


def index(request):
    latest = Reviews.objects.all()
    paginator = Paginator(latest, 10) # убрать потом посты в settings
    page = get_page(request, paginator)
    return render(request, 'reviews/index.html', {'page': page, })


@login_required()
def new_review(request):
    form_creation = formset_factory(CreationForm)
    form_review = formset_factory(ReviewForm)
    if request.method != 'POST':
        creation_formset = form_creation(prefix='creation')
        review_formset = form_review(prefix='review')
        return render(request, 'reviews/new.html',
                      {'form_review': review_formset,
                       'from_creation':creation_formset,  
                       'operation': 'Добавить обзор',
                       'add_or_save': 'Добавить'})
    creation_formset = form_creation(request.POST or None,
                                     files=request.FILES or None,
                                     prefix='creation') 
    review_formset = form_review(request.POST or None,
                                 files=request.FILES or None,
                                 prefix='review')
    if creation_formset.is_valid() and review_formset.is_valid():
        new_creation = review_formset.save()
        new_review = review_formset.save(commit=False)
        new_review.author = request.user
        new_review.creation = new_creation
        new_review.save()
        return redirect(index)
    return render(request, 'reviews/new.html',
                  {'creation_form': creation_formset,
                   'review_form': review_formset,
                   'operation': 'Добавить обзор',
                   'add_or_save': 'Добавить', })


def review_view(request, username, review_id):
    review = get_object_or_404(Reviews,
                               author__username=username,
                               id=review_id)
    count = review.author.reviews.count
    form = CommentForm(request.POST)
    comments = review.comments.all()
    return render(request, 'reviews/review.html',
                  {'author': review.author,
                   'review': review,
                   'creation_name': review.creation.name,
                   'count': count,
                   'form': form,
                   'comments': comments})

def review_edit(request, username, review_id):
    pass

def profile(request, username):
    reviews = Reviews.objects.filter(author__author__username=username)
    paginator = Paginator(reviews, 10)
    page = get_page(request, paginator)
    return render(request, 'reviews/profile.html',
                  {'author': username, 'page': page,
                   'count':  reviews.count})


def add_comment(request, username, review_id):
    pass

def creation(request, slug='1'):
    creation = get_object_or_404(Creations, slug=slug)
    reviews = creation.reviews.all()
    paginator = Paginator(reviews, 10)
    page = get_page(request, paginator)
    # еще вот тут рейтинг не плохо посчитать
    # значение вывести в шаблон
    return render(request, 'reviews/creation.html', 
                  {'creation': creation, 'page': page})
