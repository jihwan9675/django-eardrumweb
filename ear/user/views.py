from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import User

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('userid')        
        return super().form_valid(form)

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login/'


    def form_valid(self, form):
        user = User(
            userid = form.data.get('userid'),
            username = form.data.get('username'),
            password = make_password(form.data.get('password')),
        )
        return super().form_valid(form)