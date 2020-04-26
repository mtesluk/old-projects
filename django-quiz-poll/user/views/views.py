from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from ..forms import UserRegistrationForm


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html', {'section': 'dashboard'})


@login_required
def panel(request):
    return render(request, 'user/panel.html')


@login_required
def password_change_done(request):
    return render(request, 'user/password_change_done.html')


def password_reset_done(request):
    return render(request, 'user/password_reset_done.html')


def password_reset_complete(request):
    return render(request, 'user/password_reset_complete.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse(("account:login")))
    else:
        user_form = UserRegistrationForm()

    return render(request, 'user/register.html', {'form': user_form})
