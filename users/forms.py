from django.contrib.auth.backends import UserModel
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"
