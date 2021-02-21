from django.shortcuts import render, redirect, get_object_or_404
import requests, json
from .forms import BookForm, SearchForm
from BookClubApp.models import Book
from django.conf.urls.static import static


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
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # get search term from form
            searchTerm = form.cleaned_data['searchTerm']
            # add search term to google books api url
            api_response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + searchTerm)
            # get json reponse
            jsonData = api_response.json()

            # open file and write json data to it
            f = open("BookClubApp/static/tmp/temp.txt", "w")
            f.write(json.dumps(jsonData, indent=1))
            f.close()

        else:
            form = SearchForm()

    return render(request, 'BookClubApp/BookClubApp_explore.html')


def BookClubApp_searchForm(request):
    context = {}
    context['form'] = SearchForm()
    return render(request, 'BookClubApp/BookClubApp_search.html', context)


# add new book
def BookClubApp_AddBook(request):
    form = BookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return to the booklist page after new book added
            return redirect('BookClubApp_bookList')
    content = {'form' : form}
    return render(request, 'BookClubApp/BookClubApp_AddBook.html', content)


# edit book
def BookClubApp_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('BookClubApp_book', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'BookClubApp/BookClubApp_edit.html', {'form' : form})


# delete book
def BookClubApp_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # if method is post, then delete the book object
    if request.method == 'POST':
        book.delete()
        # return to booklist page after deleting book
        return redirect('BookClubApp_bookList')
    context = {
        "book" : book
    }
    return render(request, 'BookClubApp/BookClubApp_delete.html', context)
