from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import *
from .forms import *
# Create your views here.

def index(request):
    todo = Tasks.objects.all()
    form = TasksForm()

    if request.method =='POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todo': todo, 'form': form}
    return render(request, 'list.html', context)

def updateList(request, pk):
    updatedTask = Tasks.objects.get(id=pk)

    form = TasksForm(instance=updatedTask)

    if request.method =='POST':
        form = TasksForm(request.POST, instance=updatedTask)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'update_list.html', context)


def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')


    context = {'item': item}
    return render(request, 'delete.html', context)