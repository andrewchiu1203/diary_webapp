from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from .forms import DiaryForm
from main.models import Diary

def blank(request):
    return redirect(reverse_lazy("main:index"))

def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))
    
    search_input = request.GET.get("search-area") or ""

    if search_input:
        diarys = Diary.objects.filter(user = request.user, title__icontains = search_input)
    else:
        diarys = Diary.objects.filter(user = request.user)

    return render(request, "main/index.html", {
        "diarys" : diarys,
    })
    
def signin(request):
    error = False

    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("main:index"))
            
            error = "Incorrect Credentials"
        
        return render(request, "main/signin.html", {
            "error" : error,
        })
    
    return redirect(reverse_lazy("main:index"))

def signup(request):
    error = False

    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            re_password = request.POST["re_password"]

            # Check create user info and error
            if username == "" or password == "" or re_password == "":
                error = "Please fill out every box"
            elif password != re_password:
                error = "Passwords don't match"
            elif len(User.objects.filter(username = username)) != 0:
                error = "Username already exist"
            else:
                User.objects.create_user(username = username, password = password).save()
                return redirect(reverse_lazy("main:signin"))
 
        return render(request, "main/signup.html", {
            "error" : error,
        })
    
    return redirect(reverse_lazy("main:index"))

def signout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect(reverse_lazy("main:signin"))

def update(request, current_id):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))

    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        Diary.objects.filter(id = current_id, user = request.user).update(title = new_title)
        Diary.objects.filter(id = current_id, user = request.user).update(body = new_body)

    diary = Diary.objects.get(id = current_id, user = request.user)
    form = DiaryForm(instance = diary)
    if form.is_valid():
        form.save()

    return render(request, "main/update.html", {
        "diary" : diary,
        "form" : form,
    })

def create(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))
    
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        Diary(user = request.user, title = new_title, body = new_body).save()

        return redirect(reverse_lazy("main:index"))
    
    return render(request, "main/create.html", {
        "form" : DiaryForm(),
    })

def delete(request, current_id):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))
    
    if request.method == "POST":
        Diary.objects.get(id = current_id, user = request.user).delete()
        return redirect(reverse_lazy("main:index"))

    return render(request, "main/delete.html", {
        "diary" : Diary.objects.get(id = current_id, user = request.user)
    })
