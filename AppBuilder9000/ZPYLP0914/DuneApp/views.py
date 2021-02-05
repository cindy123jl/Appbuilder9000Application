from tkinter import NONE

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .form import BookForm
from django.core.paginator import Paginator


def DuneApp_home(request):
    return render(request, "DuneApp/DuneApp_home.html")


def DuneApp_createbook(request):
    form = BookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('DuneApp_home')
    context = {'form': form}
    return render(request, "DuneApp/DuneApp_createbook.html", context)


def BookIndex(request):
    all_books = Book.Books.all()

    paginator = Paginator(all_books, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'DuneApp/DuneAppBook_index.html', {'page_obj': page_obj})

def BookDetails(request, pk):
    bookdtl = get_object_or_404(Book, pk=pk)
    book_details = {'bookdtl': bookdtl}
    return render(request, 'DuneApp/DuneApp_details.html', book_details)