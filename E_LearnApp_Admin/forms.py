from django.forms import ModelForm

from Account.models import CustomUser
from E_LearnApp_Admin.models import Subject


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("pp", "username", "first_name", "last_name", "email", "is_superuser")

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ("name_subject", "description_subject", "photo_subject")
