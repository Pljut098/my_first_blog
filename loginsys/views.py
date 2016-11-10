import json

import simplejson as simplejson
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.contrib import messages
# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from registration.forms import RegistrationFormUniqueEmail

from loginsys.forms import UserForm, LoginForm
from loginsys.models import MyUser


def login(request):
    args={}
    args.update(csrf(request))
    login_form = LoginForm()
    args['login_form'] = login_form
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = "User is not found"
                return render(request, 'loginsys/login.html', args)
        else:
            args['login_form'] = login_form
            args['login_error'] = "login error"
            return render(request, 'loginsys/login.html', args)

    return render(request, 'loginsys/login.html', args)

def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)




def register(request):
    args = {}
    args.update(csrf(request))
    user_form = UserForm()

    args['user_form'] = user_form


    if request.POST:
        user_form = UserForm(request.POST)
    if user_form.is_valid():
        model_instance = user_form.save(commit=False)
        model_instance.password = make_password(model_instance.password, salt=None, hasher='default')
        user = model_instance
        user.save()
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        auth.login(request, user)

        return redirect('/')
    #     else:
    #         args['user_form'] = user_form
    #
    #         args['login_error'] = "Register error"
    #         return render(request, 'loginsys/register.html', args)
    return render(request, 'loginsys/register.html', args)



