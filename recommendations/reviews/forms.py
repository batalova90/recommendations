from django.forms import ModelForm, Textarea

from .models import Reviews, Comment, Creations


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'name']
        labels = {'text': 'Текст обзора',
                  'name': 'Название обзора',
                  'creation': 'Произведение'}
        help_texts = {'text': 'Введите текст обзора',
                      'name': 'Введите название обзора',}


class CreationForm(ModelForm):
    class Meta:
        model = Creations
        fields = ['name', 'genre', 'category']
        labels = {'name': 'Название произведения',
                  'genre': 'Жанр',
                  'category': 'Категория'}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        labels = {'text': 'Текст комментария', }
        widget = {'text': Textarea(attrs={'class': 'form-control'}), }
