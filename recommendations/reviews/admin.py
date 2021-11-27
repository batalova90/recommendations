from django.contrib import admin
from django.shortcuts import redirect
from .models import Reviews, Genres, Categories, Creations, Authors, RaitingReview

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'name', 'creation')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = ('-empty-')


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('slug',)
    list_filter = ('slug', )
    empty_value_display = ('-empty-')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('slug', )
    list_filter = ('slug', )
    empty_value_display = ('-empty-')


class CreationsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'slug')
    search_fields = ('name',)
    list_filter = ('name', )
    empty_value_display = ('-empty-')


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'raiting', 'author_card')

    def author_card(self, obj):
        return redirect('profile', 'author')


class RaitingReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'raiting', 'user')
    empty_value_display = ('-empty-')


admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Creations, CreationsAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(RaitingReview, RaitingReviewAdmin)
