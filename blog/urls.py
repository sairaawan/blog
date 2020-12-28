"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site
from post.views import index, blog, post, search, post_create, post_update, post_delete,contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
    path('', index),
    path('blog/', blog, name='post_list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post_create'),
    path('post/<id>/', post, name='post_detail'),
    path('post/<id>/update/', post_update, name='post_update'),
    path('post/<id>/delete/', post_delete, name='post_delete'),
    path('contact/', contact_view, name='contact_view'),
    path('', include('allauth.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)