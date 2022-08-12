from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import get_user_model
User = get_user_model()


def homepage(request):
    return render(request, 'base.html')


class MyLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthUserForm

    def get_success_url(self):
        return reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


class MyLogoutView(LogoutView):
    new_page = reverse_lazy('home')
