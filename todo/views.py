from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        #create user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasklist')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',{'form': UserCreationForm(), 'error': 'Username has already been taken. Please use a different username'})
        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})
            #tell user password didnt match


@login_required()
def tasklist(request):
    tasks = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/tasklist.html', {'tasks': tasks})


@login_required()
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required()
def home(request):
    return render(request, 'todo/home.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username not found...'})
        else:
            login(request, user)
            return redirect('tasklist')

@login_required()
def createtask(request):
    if request.method == 'GET':
        return render(request, 'todo/createtask.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('tasklist')
        except ValueError:
            return render(request, 'todo/createtask.html', {'form': TodoForm(), 'error':'Bad data passed in'})

#VIEW TASK LIST
@login_required()
def viewtask(request, todo_pk):
    viewing = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=viewing)
        return render(request, 'todo/viewtask.html', {'viewing': viewing, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=viewing)
            form.save()
            return redirect('tasklist')
        except ValueError():
            return render(request, 'todo/viewtask.html', {'viewing': viewing, 'form': form, 'error':'Bad info'})

@login_required()
def completetask(request, todo_pk):
    viewing = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        viewing.datecompleted = timezone.now()
        viewing.save()
        return redirect('tasklist')

@login_required()
def deletetask(request, todo_pk):
    viewing = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        viewing.delete()
        return redirect('tasklist')

@login_required()
def completed(request):
    todo = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completed.html', {'todos': todo})