from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from BookClubApp.models import Book


def BookClubApp_home(request):
    return render(request, 'BookClubApp/BookClubApp_home.html')


def BookClubApp_booklist(request):
    # will return read book items from database
    data = Book.objects.all()
    books = {
        "books": data
    }
    return render(request, 'BookClubApp/BookClubApp_booklist.html', books)


def BookClubApp_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'BookClubApp/BookClubApp_book.html', context={'book': book})


def BookClubApp_explore(request):
    # will return wishlist books from database
    return render(request, 'BookClubApp/BookClubApp_explore.html')


def BookClubApp_AddBook(request):
    form = BookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return to the booklist page after new book added
            return redirect('BookClubApp_bookList')
    content = {'form' : form}
    return render(request, 'BookClubApp/BookClubApp_AddBook.html', content)

