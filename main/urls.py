from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('blog_2.urls')),
    path('', include('book.urls')),
    path('', include('myShop.urls')),
    path('', include('tour.urls')),
    path('', include('anketa.urls')),
    path('', include('users.urls')),
    path('', include('CineBoard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)