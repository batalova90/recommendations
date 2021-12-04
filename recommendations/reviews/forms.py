from django.forms import ModelForm, Textarea
from django import forms
from django_bootstrap_datetimepicker.widgets import BootstrapDateTimeInput
from .models import Reviews, Comment, Creations, RaitingReview, Pictures, ReviewPicture
from cloudinary.forms import CloudinaryFileField

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'name', 'image']
        labels = {'text': 'Текст',
                  'name': 'Название обзора',
                  'image': 'Картинка'}
        help_texts = {'text': 'Введите текст обзора',
                      'name': 'Введите название обзора',
                      'picture': 'Выберите изображение'}


class CreationForm(ModelForm):
    class Meta:
        model = Creations
        fields = ['name', 'rating', 'category', 'slug']
        labels = {'name': 'Название произведения',
                  'rating': 'Рэйтинг',
                  'category': 'Категория',
                  'slug': 'slug'}
        help_texts = {'name': 'Введите название произведения',
                      'slug': 'Введите slug'}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        labels = {'text': 'Текст комментария', }
        widget = {'text': Textarea(attrs={'class': 'form-control'}), }


class RaitingReviewForm(forms.ModelForm):
    class Meta:
        model = RaitingReview
        fields = ['raiting',]
        #widget = {'raiting': forms.ChoiceField(widget=forms.RadioSelect, choices=RAITING)}
        #widgets = {'raiting': forms.NumberInput(attrs={'max': '5', 'class': 'form-control'})}


class SearchForm(forms.Form):
    query = forms.CharField()
    class Meta:
        labels = {'query': 'Искать'}


class PictureForm(ModelForm):
    class Meta:
        model = Pictures
        fields = '__all__'

