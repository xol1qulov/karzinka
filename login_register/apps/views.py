from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from apps.forms import UsersForm, UsersFormEdit
from apps.models import User


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UsersForm()

    return render(request, 'register.html', {'form': form})


def edit_views(request, pk):
    contact = User.objects.filter(id=pk).first()
    if request.POST:
        form = UsersFormEdit(request.POST, files=request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'edit.html', {'contact': contact})



