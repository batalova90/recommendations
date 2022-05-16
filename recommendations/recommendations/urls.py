from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'reviews.views.page_not_found' #noqa
handler500 = 'reviews.views.server_error' #noqa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace="about")),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include("reviews.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
