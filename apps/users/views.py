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
        return redirect('/friends')
    except:
        messages.add_message(request, messages.INFO,"Please login\n")
        return redirect("/main")

def show(request,id):
    single_user = User.objects.get(id = id)
    data = {
        "single_user": single_user,
    }
    return render(request,'users/success.html',data)

def friend(request):
    x = User.objects.get(id = request.session['id'])
    all_users = User.objects.exclude(friend_by = x)
    all_friends = User.objects.filter(friend_by = x)

    data = {
        "all_users": all_users,
        "all_friends": all_friends,
        "count": all_users.count()
    }
    return render(request,'users/friends.html',data)

def friend_add(request):
    User.objects.add_friend(request.POST, request.session['id'])
    return redirect('/friends')

def friend_del(request,id):
    User.objects.del_friend(id, request.session['id'])
    return redirect('/friends')

#=============================================================#
#                      PROCESS METHODS                        #
#=============================================================#
def create(request):
    error = User.objects.validate(request.POST)
    if error:
        for x in error:
            messages.add_message(request, messages.INFO,x)
        return redirect("/main")
    else:
        single_user = User.objects.new(request.POST)
        request.session['id'] = single_user.id
        request.session['first_name'] = single_user.first_name
        request.session['last_name'] = single_user.last_name
        return redirect("/users/success")

def login(request):
    single_user = User.objects.login_validate(request.POST)
    if single_user:
        request.session['id'] = single_user.id
        request.session['first_name'] = single_user.first_name
        request.session['last_name'] = single_user.last_name
        return redirect("/users/success")
    else:
        messages.add_message(request, messages.INFO,"Login fail\n")
        return redirect("/main")

def logout(request):
    request.session.clear()
    return redirect("/main")

