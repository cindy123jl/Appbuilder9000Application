from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


# Create your views here.
def home(request):
    """Function to open the homepage."""
    return render(request, 'ItemsApp/home.html')


def new_item(request):
    """Creates the form used for user input"""
    form = ItemForm(data=request.POST or None)  # Creates the form from forms.py.
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('itemsApp_home')  # When the form is created, redirect to the home page.
    content = {'form': form}  # Dictionary for form data entry.
    return render(request, 'ItemsApp/new_item.html', content)


def display_items(request):
    """Creates a form displaying the current items in the database."""
    item = Item.objects.all().values()  # Grabs all values from all items in the database.
    content = {'item': item}  # Dictionary for the items.
    return render(request, 'ItemsApp/display_items.html', content)


def select_item(request):
    """Creates a list of items from the database with anchor tag to select."""
    item_list = Item.objects.all()  # Grabs all items from all items in the database.
    content = {'item_list': item_list}
    return render(request, "ItemsApp/details.html", content)


def item_details(request, pk):
    """Displays the chosen item from 'select_item' function."""
    pk = int(pk)
    item_get = Item.objects.filter(pk=pk)
    content = {'item_get': item_get}
    return render(request, "ItemsApp/details_page.html", content)





