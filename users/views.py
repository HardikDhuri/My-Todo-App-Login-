from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from tasks.models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, "users/register.html", context)
