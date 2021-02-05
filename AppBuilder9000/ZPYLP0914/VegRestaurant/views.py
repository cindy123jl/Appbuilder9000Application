from tkinter.ttk import Entry

from django.shortcuts import render, get_object_or_404, redirect

from . import models
from .forms import OrderForm
# Create your views here.
from .models import Order


def home(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, 'VegRestaurant/VR_home.html')

def createOrder(request):
    form = OrderForm(data=request.POST or None)

    if form.is_valid():
        print("Form is valid")
        form.save()
        return redirect('VegRestauranthome')
    else:
        print(form.errors)
        form = OrderForm()
    context = {'form': form}
    return render(request, 'VegRestaurant/VR_createOrder.html', context)

def VR_index(request):
# gets all orders from database
    order = Order.objects.all()
# print to terminal to make sure data is populating
    print(order)
# creates dictionary for items in the database and passes the args to the page
    context = {'order': order }
    return render(request, 'VegRestaurant/VR_data.html', context)

def VR_details(request,order_id):
# gets all orders from database
    order = Order.objects.get(id=order_id)
# print to terminal to make sure data is populating
    print(order)
# creates dictionary for items in the database and passes the args to the page
    context = {'order': order }
    return render(request, 'VegRestaurant/VR_details.html', context)