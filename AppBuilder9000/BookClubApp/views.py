from django.shortcuts import render, redirect


def BookClubApp_home(request):
    return render(request, 'BookClubApp/BookClubApp_home.html')


def BookClubApp_booklist(request):
    # will return read book items from database
    return


def BookClubApp_explore(request):
    # will return wishlist books from database
    return
