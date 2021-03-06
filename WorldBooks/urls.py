"""WorldBooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views

urlpatterns = [
    path('', views.index, name='front'),

    re_path(r'^books/?$', views.BookListView.as_view(), name='books'),
    re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^mybooks/?$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^book-create/?$', views.BookCreate.as_view(), name='book-create'),
    re_path(r'^book-update/(?P<pk>\d+)/?$', views.BookUpdate.as_view(), name='book-update'),
    re_path(r'^book-delete/(?P<pk>\d+)/?$', views.BookDelete.as_view(), name='book-delete'),

    re_path(r'^authors/?$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^authors-add/?$', views.authors_add, name='author-add'),
    path('author-edit/<int:id>/', views.author_edit, name='author-edit'),
    path('author-create/', views.author_create, name='author-create'),
    path('author-delete/<int:id>', views.author_delete, name='author-delete'),

    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls'))
]
