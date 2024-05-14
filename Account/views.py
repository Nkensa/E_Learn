import re

from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

# Create your views here.

User = get_user_model()

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Vous pouvez ajouter ici plus de validations selon vos besoins et pour les autres champs qui existe dans votre formulaire de register
        if email and password:  # Vérifiez que les champs ne sont pas vides
            if len(password) < 8:

                return render(request, 'Accounts/register.html', {
                    'error': 'Le mot de passe doit contenir au moins 8 caractères;\n2 lettres majuscules;\n2 lettres minuscules;\n2 chiffres;\n2 caractères spéciaux {!@#$%^&*()_\-+={}\[\]|\\:;\"\'<>,.?/};'
                })

            if not re.search(r'[A-Z].*[A-Z]', password):
                return render(request, 'Accounts/register.html', {
                    'error': 'Le mot de passe doit contenir au moins 2 lettres majuscules'
                })

            if not re.search(r'[a-z].*[a-z]', password):
                return render(request, 'Accounts/register.html', {
                    'error': 'Le mot de passe doit contenir au moins 2 lettres minuscules'
                })


            if not re.search(r'\d.*\d', password):
                return render(request, 'Accounts/register.html', {
                    'error': 'Le mot de passe doit contenir au moins 2 chiffres'
                })

            if not re.search(r'[!@#$%^&*()_\-+={}\[\]|\\:;\"\'<>,.?/]', password):
                return render(request, 'Accounts/register.html', {
                    'error': 'Le mot de passe doit contenir au moins 2 caractères spéciaux {!@#$%^&*()_\-+={}\[\]|\\:;\"\'<>,.?/}'
                })

            print(f'nom : {username}, email : {email}, password : {password} ')
            # pass
            # Créez l'utilisateur
            user = User.objects.create(username=username, email=email, password=make_password(password))
            user.save()
            login(request, user)  # Connectez l'utilisateur
            return redirect('register')  # Redirigez vers la page d'accueil
        else:
            return render(request, 'Account/register.html', {
                'error': 'Email and password are required.'
            })
    else:
        return render(request, "Account/register.html")


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Account/login.html', {
                'error': 'Invalid email or password.'
            })
    else:
        return render(request, 'Account/login.html')