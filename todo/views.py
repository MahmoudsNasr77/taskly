from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponse
from .models import Task
from .forms import TaskForm, UserForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)  # Changed to 'tasks'
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user=request.user
            form.save()
            return redirect('/')
            
    return render(request, 'index.html', {'tasks': tasks,'form':form})

def singleTask(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'single.html', {'task': task})



def deleteTask(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.delete()
        return redirect('/')  # Use named URL
    return HttpResponseNotAllowed(["POST"])  # Prevents accidental GET deletions

def updateTask(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')  # Use named URL
    return render(request, 'update.html', {'form': form})


def register(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'register.html',{'form':form})
def login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                return HttpResponse('Invalid Login')
    return render(request,'login.html',{'form':form})
def logout(request):
    auth.logout(request)
    return redirect('todo:login')