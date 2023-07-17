from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from apps.forms import UserSignUpModelForm, UserChangeProfileModelForm
from apps.models import User, Message


def sign_up(request):
    if request.POST:
        form = UserSignUpModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-list')
        if errors := form.errors:
            print(errors.as_json(escape_html=True))
            return render(request, 'bs4_sign_up_page.html', {'errors': errors})
    return render(request, 'bs4_sign_up_page.html')


def sign_in(request):
    data = request.POST
    if data:
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('my-profile')
    return render(request, 'bs4_beta_login.html')


def users_list(request):
    users = User.objects.order_by('-last_login')
    return render(request, 'profile-card.html', {'users': users})


# @login_required
def my_profile(request):
    user = request.user
    if user.is_anonymous:
        return redirect('sign-in')
    if request.POST:
        form = UserChangeProfileModelForm(request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            # User.objects.filter(id=request.user.id).update(**form.cleaned_data)
            form.save()

    return render(request, 'profile-view.html')


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'profile-view.html', {'user': user})


@login_required
def chat(request, user_id):
    messages = Message.objects.filter(
        Q(author_id=request.user.id, to_id=user_id) |
        Q(author_id=user_id, to_id=request.user.id)
    ).order_by('created_at')
    if request.POST:
        text = request.POST.get('text')
        to_user = User.objects.filter(id=user_id).first()
        if to_user and text:
            Message.objects.create(author=request.user, to=to_user, text=text)
    return render(request, 'bs4_simple_chat_app.html', {'messages': messages})
