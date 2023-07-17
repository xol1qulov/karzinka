from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsersForm
from .models import Contact


def home(request):
    contact = Contact.objects.all()
    return render(request, 'home.html', {'contact': contact})


def home_red(request):
    contact = Contact.objects.all()
    return render(request, 'home_red.html', {'contact': contact})


def user(request, pk):
    contact = Contact.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'profil.html', {'contact': contact})


def create(request):
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user', pk=form.instance.pk)
    else:
        form = UsersForm()

    return render(request, 'create.html', {'form': form})


def delete_user(request, pk):
    user = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect('/')

    context = {'user': user}
    return render(request, 'home.html', context)
