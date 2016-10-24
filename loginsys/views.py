from django.contrib import auth
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User is not found"
            return render(request, 'loginsys/login.html', args)
    else:
        return render(request, 'loginsys/login.html', args)

def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return  render(request, 'loginsys/register.html', args)