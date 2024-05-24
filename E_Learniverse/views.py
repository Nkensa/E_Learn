from django.shortcuts import render, get_object_or_404, redirect

from Account.models import CustomUser
from E_LearnApp_Admin.models import Classroom, Subject
from E_Learniverse.models import Adventure


# Create your views here.

def welcomeApp(request):
    selected = 'WelcomeApp'


    if request.method == 'POST':
        classroom_id = request.POST.get('classroom')
        classroom = Classroom.objects.get(pk=classroom_id)

        subjects_ids = request.POST.getlist('subjects')
        user = request.user

        adventure = Adventure.objects.create(classroom=classroom, user=user)
        subjects = Subject.objects.filter(id_subject__in=subjects_ids)
        adventure.subjects.set(subjects)
        adventure.save()
        return redirect('my_adventure')
    else:
        classrooms = Classroom.objects.all()
        subjects = Subject.objects.all()

    return render(request, 'E_Learniverse/welcome_app.html', {'classrooms': classrooms, 'subjects': subjects, 'selected': selected})


def profil(request):
    selected = 'profil'
    # user = get_object_or_404(CustomUser)

    return render(request, 'E_Learniverse/profil.html')


def my_adventure(request):
    selected = 'adventure'
    user = request.user
    adventures = Adventure.objects.filter(user=user)

    return render(request, 'E_Learniverse/adventure_detail.html', {'adventures': adventures, 'selected': selected})

def profil_user(request, pk):
    selected = 'profil'
    try:
        user = get_object_or_404(CustomUser, id_CustomUser=pk)
        return render(request, 'E_Learniverse/profil.html', {'user': user, 'selected': selected})
    except CustomUser.DoesNotExist:
        return render(request, 'E_Learniverse/profil.html', {'user': None, 'selected': selected})

# def adventure_detail(request, pk):
#     adventure = Adventure.objects.get(adventure_id=pk)
#     selected_subjects = adventure.subjects.all()
#
#     return render(request, 'E_Learniverse/adventure_detail.html', {'adventure': adventure, 'selected_subjects': selected_subjects})
