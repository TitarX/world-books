from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *


def index(request):
    # Получение количества записей
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    # Количество доступных книг
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, 'catalog/front.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
