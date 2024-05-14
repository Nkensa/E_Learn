from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from Account.models import CustomUser
from E_LearnApp_Admin.forms import CustomUserForm
from E_LearnApp_Admin.models import *


# from E_LearnApp.models import Classroom, Subject

# Create your views here.


def WelcomeAdmin(request):
    selected = 'home'

    return render(request, "E_LearnApp_Admin/home_page_admin.html", locals())

def Users_list(request):
    selected = 'users'
    users_list = CustomUser.objects.all()

    # Pagination : 08 éléments par page
    paginator = Paginator(users_list.order_by('date_joined'), 7)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        users_list = paginator.page(page)
    except EmptyPage:
        users_list = paginator.page(paginator.num_pages())
    return render(request, "E_LearnApp_Admin/users_list.html", locals())


# class CreateUser(CreateView):
#     model = CustomUser
#     form_class = CustomUserForm
#     template_name = "E_LearnApp_Admin/users_forms.html"
#
#     def get_success_url(self):
#         return reverse_lazy("detail_user", kwargs=("pk", self.object.id_CustomUser))


def detail_user(request, pk):
    user = get_object_or_404(CustomUser, id_CustomUser=pk)

    return render(request, 'E_LearnApp_Admin/user_detail.html', {'user': user})

def update_user(request, pk):
    object = True
    user = get_object_or_404(CustomUser, id_CustomUser=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('myusers')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'E_LearnApp_Admin/users_forms.html', {'object': object, 'form': form, 'user': user})


def create_user(request):
    object = False
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myusers')
    else:
        form = CustomUserForm()
    return render(request, 'E_LearnApp_Admin/users_forms.html', {'object': object, 'form': form})


def subjects(request):
    selected = 'users'
    subjects = Subject.objects.all()

    return render(request, 'E_LearnApp_Admin/subjects.html', {'subjects': subjects})


def classrooms(request):
    selected = 'classroom'
    classrooms = Classroom.objects.all()

    return render(request, 'E_LearnApp_Admin/classroom.html', {'classrooms': classrooms})


# @login_required
def edit_classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, id_classroom=classroom_id)

    if request.method == 'POST':
        name_classroom = request.POST.get('name_classroom')
        custom_users = request.POST.get('custom_user')
        subjects = request.POST.getlist('subject')

        classroom.name_classroom = name_classroom
        classroom.custom_user.clear()
        classroom.subject.clear()

        # Ajouter les utilisateurs sélectionnés
        for user_id in custom_users:
            user = CustomUser.objects.get(id_CustomUser=user_id)
            classroom.custom_user.add(user)

        # Ajouter les matières sélectionnées
        for subject_id in subjects:
            subject = Subject.objects.get(id_subject=subject_id)
            classroom.subject.add(subject)

        classroom.save()
        return redirect('classrooms')
    else:
        custom_users = CustomUser.objects.all()
        subjects = Subject.objects.all()
    return render(request, 'E_LearnApp_Admin/classroom_form.html', {'classroom': classroom, 'custom_users': custom_users, 'subjects': subjects})
