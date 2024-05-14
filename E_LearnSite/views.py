from django.core.validators import validate_email
from django.shortcuts import render, redirect


# Create your views here.

def index(request):

    return render(request, "E_LearnSite/site.html")


def sign_up(request):
    error = False
    message = ""
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print("==" * 7, " NEW POST : ", name, email, password, "==" * 7)

        try:
            validate_email(email)
        except:
            error = True
            message = "L'adresse email n'est pas valide"

        user = Users.objects.filter(email=email).first()
        if user:
            error = True
            message = "L'utilisateur existe déjà"

        if error == False:
            user = Users.objects.create(first_name=name, email=email, mot_de_passe=password, statut=1)
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