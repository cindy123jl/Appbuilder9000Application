from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, AuthorForm
from .models import Book


def home(request):
    return render(request, 'CodeBookApp/CodeBookApp_home.html')


def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('CodeBookApp_books')
    return render(request, 'CodeBookApp/CodeBookApp_add.html', {'form': form})


def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('CodeBookApp_add')
    return render(request, 'CodeBookApp/CodeBookApp_author.html', {'form': form})


def code_books(request):
    books = Book.objects.all()
    return render(request, 'CodeBookApp/CodeBookApp_books.html', {'books': books})


def book_detail(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, id=pk)
    return render(request, 'CodeBookApp/CodeBookApp_detail.html', {'book': book})


def book_edit(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, id=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('CodeBookApp_books')
        else:
            print(form.errors)
    else:
        return render(request, 'CodeBookApp/CodeBookApp_edit.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('CodeBookApp_books')
    context = {'book': book}
    return render(request, 'CodeBookApp/CodeBookApp_confirm_delete.html', context)


def confirmed(request):
    if request.method == 'POST':
        book = BookForm(request.POST or None)
        if book.is_valid():
            book.delete()
            return redirect('CodeBookApp_books')
    else:
        return redirect('CodeBookApp_books')


