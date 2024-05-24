from django.contrib import auth
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Account.models import CustomUser


# Create your views here.

def index(request):

    return render(request, "E_LearnSite/site.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = auth.authenticate(username=username, password=password)
        if auth_user:
            auth.login(request, auth_user)
            return redirect('welcome_app')

    return render(request, "E_LearnSite/login.html")


def sign_up(request):
    error = False
    message = ""
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print("==" * 7, " NEW POST : ", name, email, password, "==" * 7)

        try:
            validate_email(email)
        except:
            error = True
            message = "L'adresse email n'est pas valide"

        user = CustomUser.objects.filter(email=email).first()
        if user:
            error = True
            message = "L'utilisateur existe déjà"

        if error == False:
            user = CustomUser.objects.create(first_name=name, email=email, password=password)
            user.save()
            return redirect("login")

        #     # else:
        #     try:
        #         user = Users.objects.create(name=name, email=email, mot_de_passe=password)
        #         user.save()
        #         return HttpResponseRedirect("/learniversapp")
        #     except:
        #         error = True
        #         message = "L'utilisateur existe déjà"

    context = {
        'error': error,
        'message': message
    }
    return render(request, "E_LearnSite/register.html", context)
