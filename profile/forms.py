# coding=utf-8

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from profile.models import CustomUser


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
                max_length=30,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    email = forms.EmailField(
                widget=forms.TextInput(attrs={
                            'placeholder':'example@mail.com',
                            'class':'form-control'
                        }))
    first_name = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'placeholder':'Антон',
                            'class':'form-control',
                        }))
    last_name = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'placeholder':'Иванов',
                            'class':'form-control',
                        }))

    password1 = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    password2 = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            p = CustomUser.objects.create(user=user)
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
                max_length=30,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))

    password = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))

# class CustomUserForm(ModelForm):
#     first_name = forms.CharField(max_length=30, required=False)
#     last_name = forms.CharField(max_length=30, required=False)
    # new_dirs = forms.CharField(min_length=5,
    #                            max_length=50,
    #                            error_messages={'required': 'Миннимум 10 символов'})

#     email = forms.EmailField()
#     bio = forms.CharField()
#     date_of_birth = forms.DateTimeField(
#         label='Дата рождения',
#         widget=DatePickerWidget(params='dateFormat: "YYYY/DD/MM", minDate:"1/1/1900", pickTime: false, weekStart: 1, autoclose: 1,',
#                                 attrs={'class': 'form-control', 'onclick': 'picker()', }))

#     class Meta:
#         model = settings.AUTH_PROFILE_MODULE
#         exclude = ['user']

#     def save(self, *args, **kw):
#         super(CustomUserForm, self).save(*args, **kw)
#         self.instance.user.first_name = self.cleaned_data.get('first_name')
#         self.instance.user.last_name = self.cleaned_data.get('last_name')
#         self.instance.user.email = self.cleaned_data.get('email')
#         self.instance.user.save()