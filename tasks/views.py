from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form.save()
            return redirect('home')
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form,
    }

    return render(request, "tasks/home.html", context )



