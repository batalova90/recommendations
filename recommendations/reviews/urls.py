from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_review, name='new_review'),
    path('<str:username>/<int:review_id>/edit/',
         views.review_edit,
         name='review_edit'),
    path('<str:username>/<int:review_id>/', views.review_view,
         name='review_view'),
    path('<str:username>/<int:review_id>/comment/',
         views.add_comment, name='add_comment'),
    path('search/', views.review_search, name='search'),
    path('<str:username>/', views.profile, name='profile'),
    path('creation/<str:slug>', views.creation, name='creation'),
    path('review/<str:username>/<int:review_id>/add_raiting/',
         views.add_review_raiting,
         name='add_review_raiting'),
    path('top_10/authors', views.top_authors, name="top_10_authors"),
]
