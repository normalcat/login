from django.shortcuts import render, redirect
import bcrypt
import re
from models import *
from django.contrib import messages

#=============================================================#
#                       RENDER METHODS                        #
#=============================================================#
def index(request):
    return render(request,"users/index.html")

def success(request):
    try:
        single_user = User.objects.get(id = request.session['id'])
        data = {
            "single_user": single_user
        }
        return render(request,"users/success.html", data)
    except:
        messages.add_message(request, messages.INFO,"Please login\n")
        return redirect("/users")

#=============================================================#
#                      PROCESS METHODS                        #
#=============================================================#
def create(request):
    error = User.objects.validate(request.POST)
    print error
    if error:
        for x in error:
            messages.add_message(request, messages.INFO,x)
        return redirect("/users")
    else:
        single_user = User.objects.new(request.POST)
        request.session['id'] = single_user.id
        return redirect("/users/success")

def login(request):
    single_user = User.objects.login_validate(request.POST)
    if single_user:
        request.session['id'] = single_user.id
        return redirect("/users/success")
    else:
        messages.add_message(request, messages.INFO,"Login fail\n")
        return redirect("/users")

def logout(request):
    request.session.clear()
    return redirect("/users")