from django.shortcuts import render, get_object_or_404
from book_outlet.models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    list_books = Book.objects.all()
    total_no_of_books = list_books.count()
    average_book_rating = list_books.aggregate(Avg('rating'))

    return render(request, 'book_outlet/index.html',
                  {
                      'list_books': list_books,
                      'total_no_of_books': total_no_of_books,
                      'average_book_rating': average_book_rating,
                  })


def book_detail(request, slug):
    if (id):
        book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {'book': book})
