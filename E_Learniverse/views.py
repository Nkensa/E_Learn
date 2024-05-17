from django.shortcuts import render, get_object_or_404

from Account.models import CustomUser


# Create your views here.

def welcomeApp(request):
    selected = 'WelcomeApp'
    # user = get_object_or_404(CustomUser)

    return render(request, 'E_Learniverse/welcome_app.html')


def profil(request, pk):
    selected = 'profil'
    user = get_object_or_404(CustomUser, id_CustomUser=pk)

    return render(request, 'E_Learniverse/profil.html', {'user': user})
