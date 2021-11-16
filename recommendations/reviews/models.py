import textwrap

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# разобраться с тегами

class Genres(models.Model):
    name = models.CharField('Name of gere',
                            max_length=50,
                            unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('id', )

    def __str__(self):
        return self.slug


class Categories(models.Model):
    name = models.CharField('Name of categories',
                            max_length=50,
                            unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id', )

    def __str__(self):
        return self.slug


class Creations(models.Model):
    name = models.CharField('Name of titles',
                            max_length=200)
    genre = models.ManyToManyField(Genres,
                                   through='CreationsGenres')
    category = models.ForeignKey(Categories,
                                 related_name='categories',
                                 on_delete=models.SET_NULL,
                                 null=True)
    rating = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'Creation'
        verbose_name_plural = 'Creations'
        ordering = ('id', )

    def __str__(self):
        return self.slug


class CreationsGenres(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Creations, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre.slug


class Authors(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='raiting')
    raiting = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('raiting', ) # ??? calculation???
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.author.username

class Reviews(models.Model):
    raiting = models.IntegerField(default=0)
    author = models.ForeignKey(Authors,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    name = models.CharField('Title of review', max_length=200)
    creation = models.ForeignKey(Creations,
                                 on_delete=models.CASCADE,
                                 related_name='reviews')
    pub_date = models.DateTimeField("Date published",
                                    auto_now_add=True)
    text = models.TextField()
    
    # image!!!

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ('-pub_date',)

    def __str__(self):
        cropped_text = textwrap.shorten(
                self.text,
                width=100,
                placeholder='...'
        )
        return f'{self.name} {cropped_text}' 


class Comment(models.Model):
    review = models.ForeignKey(Reviews,
                               on_delete=models.CASCADE,
                               related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    created = models.DateTimeField('date_published', auto_now_add=True)

    class Meat:
        ordering = ('created', )
