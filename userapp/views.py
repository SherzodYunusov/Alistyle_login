from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

class LoginView(View):
    def post(self, request):
        user = authenticate(
        username = request.POST.get('u'),
        password = request.POST.get('p'),
        )
        if user is None:
            messages.success(request, 'Login yoki parolda xatolik bor')
            return redirect('/userapp/qoshish/')
        login(request, user)
        return redirect('/asosiy/')

    def get(self, request):
        return render(request, 'page-user-login.html')

class RegisterView(View):
    def post(self, request):
        if request.method == 'POST' and request.POST.get('p') == request.POST.get('p2'):
            u = User.objects.create_user(
                username=request.POST.get('u'),
                password=request.POST.get('p')
            )
            Account.objects.create(
                jins = request.POST.get('gender'),
                shahar = request.POST.get('shaxar'),
                davlat = request.POST.get('davlat'),
                user = u
            )
            return redirect('/qoshish/')
    def get(self, request):
        return render(request, 'page-user-register.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')




# Create your views here.
