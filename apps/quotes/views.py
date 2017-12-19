from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
# Create your views here.

def index(request):
    try:
        single_user = User.objects.get(id = request.session['id'])
        data = {
            "single_user": single_user
        }
    except:
        messages.add_message(request, messages.INFO,"Please login\n")
        return redirect("/main")

    all_quotes = Quote.objects.all()
    for quote in all_quotes:
        print quote
    #data = {
    #    "all_users": all_users
    #}
    all_quotes = {}
    data = {
        "all_quotes": all_quotes
    }
    
    return render(request, "quotes/index.html", all_quotes)

def add(request):
    Quote.objects.add(request.POST)
    return redirect("/quotes")

def show(request,id):
    all_quotes = Quote.objects.filter(posted_by = id)
    for quote in all_quotes:
        print quote
    data = {
        "all_quotes": all_quotes
    }
    return render(request, "quotes/show.html", all_quotes)