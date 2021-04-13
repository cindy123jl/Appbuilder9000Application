from django.shortcuts import render, redirect
from .forms import RestaurantForm


def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')


def new_restaurant(request):
    form = RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('MyThai_home')
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add.html', content)
