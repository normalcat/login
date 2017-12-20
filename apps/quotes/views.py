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
    all_favorites = Quote.objects.filter(liked_by = request.session['id'])
    data = {
        "all_quotes": all_quotes,
        "all_favorites": all_favorites
    }
    return render(request, "quotes/index.html", data)

def add(request):
    error = Quote.objects.add_(request.POST, request.session['id'])
    if error:
        for x in error:
            messages.add_message(request, messages.INFO,x)

    return redirect("/quotes")

def show(request,id):
    all_quotes = Quote.objects.filter(posted_by = id)
    count = Quote.objects.filter(posted_by = id).count()
    data = {
        "all_quotes": all_quotes,
        "count": count
    }
    return render(request, "quotes/show.html", data)

def favorite(request):
    single_quote=Quote.objects.favorite(request.POST, request.session['id'])
    print single_quote.message
    return redirect("/quotes")
