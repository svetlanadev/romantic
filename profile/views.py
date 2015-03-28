# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from profile.models import CustomUser
from profile.forms import UserCreateForm, UserLoginForm
from django.contrib.auth.decorators import login_required


class ProfileListView(ListView):
    model = CustomUser
    context_object_name = 'users'
    # Под данным именем наш список статей будет доступен в шаблоне


class ProfileDetailView(DetailView):
    model = CustomUser

    context_object_name = 'profile'


class RegisterFormView(FormView):
    form_class = UserCreateForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration_form.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = UserLoginForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


def government(request):
    users = CustomUser.objects.filter(goverment=True)
    data = {'users': users}
    return render_to_response('profile/government.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def profile(request):
    profile = CustomUser.objects.get(user=request.user)
    data = {'profile': profile}
    return render_to_response('profile.html',
                              data,
                              context_instance=RequestContext(request))