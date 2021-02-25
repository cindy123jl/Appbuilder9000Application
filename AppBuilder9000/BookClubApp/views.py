from django.shortcuts import render, redirect, get_object_or_404
import requests, json
from .forms import BookForm, SearchForm, WishlistForm
from BookClubApp.models import Book
from django.http import HttpResponse
from django import template

register = template.Library()


# display home page template
def BookClubApp_home(request):
    return render(request, 'BookClubApp/BookClubApp_home.html')


# display a list of books that the user has read (read=True)
def BookClubApp_booklist(request):
    # will return read book items from database
    data = Book.objects.filter(read=True)
    books = {
        "books": data
    }
    return render(request, 'BookClubApp/BookClubApp_booklist.html', books)


# display an individual book
def BookClubApp_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'BookClubApp/BookClubApp_book.html', context={'book': book})


# get the value from the search form and display the results from the api
def BookClubApp_explore(request):
    if request.method == 'POST':
        form = SearchForm(data=request.POST or None)

        if form.is_valid():
            # get search term from form
            searchTerm = form.cleaned_data['searchTerm']
            # add search term to google books api url
            api_response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + searchTerm + '&maxResults=20')
            # get json response
            jsonData = api_response.json()['items']

            # create a dictionary for all values
            responseData = {}
            # iterate through response and add them to the dictionary
            for i in range(len(jsonData)):
                # create dictionary for this iteration of the for loop
                indvResponse = {}
                # try blocks are necessary for results to display correctly.
                # Some results do not have all of the fields and will give a
                # KeyError if this is not included.
                # get imagelinks
                try:
                    indvResponse['imageLink'] = jsonData[i]['volumeInfo']['imageLinks']['thumbnail']
                except KeyError:
                    indvResponse['imageLink'] = ''
                # get title
                try:
                    indvResponse['title'] = jsonData[i]['volumeInfo']['title']
                except KeyError:
                    indvResponse['title'] = ''
                # get authors
                try:
                    indvResponse['authors'] = jsonData[i]['volumeInfo']['authors']
                except KeyError:
                    indvResponse['authors'] = ''
                # get description
                try:
                    indvResponse['description'] = jsonData[i]['volumeInfo']['description']
                except KeyError:
                    indvResponse['description'] = ''
                # add field values to the overall response dictionary
                responseData[i] = indvResponse;

            # create a dictionary of the overall response dictionary (responseData),
            # the search term from the search form (searchTerm)
            # and the WishlistForm (form)
            # for display on the BookClubApp_explore.html page
            context = {
                'responseData': responseData,
                'searchTerm': searchTerm,
                'form': WishlistForm(),
            }

        else:
            # if form is not valid, return to the search page
            return redirect('BookClubApp_searchForm')

    return render(request, 'BookClubApp/BookClubApp_explore.html', context)


# display the search form on the search.html page
def BookClubApp_searchForm(request):
    context = {}
    context['form'] = SearchForm()
    return render(request, 'BookClubApp/BookClubApp_search.html', context)


# add new book to the database
def BookClubApp_AddBook(request):
    form = BookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return to the booklist page after new book added
            return redirect('BookClubApp_bookList')
    content = {'form' : form}
    return render(request, 'BookClubApp/BookClubApp_AddBook.html', content)


# edit book from the database
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


# delete book from the database
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


# add new book to wishlist
def BookClubApp_AddBookWishlist(request):
    form = WishlistForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return to the wishlist page after new book added
            return redirect('BookClubApp_wishlist')
    content = {'form' : form}
    return render(request, 'BookClubApp/BookClubApp_AddBook.html', content)


# display a list of books the user has not read (read=False)
def BookClubApp_wishlist(request):
    # will return book items from database where read is false
    data = Book.objects.filter(read=False)
    books = {
        "books": data
    }
    return render(request, 'BookClubApp/BookClubApp_wishlist.html', books)

# authors returned from the api can be a list,
# so this method allows you cut characters from the string in the template
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')