from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import User

def index(request):
    return render(request, 'index.html', {'username':request.session.get('user')})

def logout(request):    
    del(request.session['user'])
    return redirect('/')

def annotation(request):
    return render(request, 'via.html', {'username':request.session.get('user')})

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
        user.save()
        
        return super().form_valid(form)