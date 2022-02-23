from django.shortcuts import render, reverse, redirect
from .models import Book
from itertools import groupby


all_books = Book.objects.all()
pub_date_list = [book.pub_date for book in all_books]
pub_date_list.sort()
new_pub_date_list = [el for el, _ in groupby(pub_date_list)]


def index(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': all_books
    }
    return render(request, template, context)


def pagi(request, pub_date):
    template = 'books/books_list_2.html'
    books = Book.objects.filter(pub_date__contains=pub_date)
    pub_date_index = new_pub_date_list.index(pub_date)
    count = len(new_pub_date_list)
    if pub_date_index == 0:
        date_next = new_pub_date_list[1]
        date_previous = None
    elif pub_date_index + 1 == count:
        date_next = None
        date_previous = new_pub_date_list[pub_date_index - 1]
    else:
        date_next = new_pub_date_list[pub_date_index + 1]
        date_previous = new_pub_date_list[pub_date_index - 1]
    context = {
        'books': books,
        'all_books': all_books,
        'date_next': date_next,
        'date_previous': date_previous
    }
    return render(request, template, context)
