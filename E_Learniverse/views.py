from django.shortcuts import render

# Create your views here.

def welcomeApp(request):
    selected = 'WelcomeApp'

    return render(request, 'E_Learniverse/welcome_app.html', locals())

