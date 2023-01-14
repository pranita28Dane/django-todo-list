from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been added to list successfully!'))
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})    
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ('The item has been deleted successfully!'))
    return redirect('home')

def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, item_id):
    if request.method == "POST":
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been edited successfully!'))
            return redirect('home')   
    else:
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})
