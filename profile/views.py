# coding: utf-8
# author: dlyapun

from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.core import signing
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from materials.models import Material
from power_comments.models import PowerComment
from profile.forms import UserCreateForm, UserLoginForm, CustomUserForm, RestartPasswordForm
from profile.models import CustomUser
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
import random
import string


class ProfileListView(ListView):
    model = CustomUser
    context_object_name = 'users'


class ProfileDetailView(DetailView):
    model = CustomUser
    context_object_name = 'profile'


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/registration_complete/"
    template_name = "registration_form.html"

    def form_valid(self, form):
        form.save()
        last_user = CustomUser.objects.last()
        last_user.user.is_active = False
        last_user.user.save()
        value = signing.dumps({"id": last_user.user.id})
        x = value.replace(':', '___')
        message = _email_message(x)
        try:
            send_mail("Регистрация на сайте tkr.od.ua",
                      message,
                      'support@tkr.od.ua',
                      [last_user.user.email],
                      fail_silently=False)
        except BadHeaderError:
            pass
            print "NOW WORKING"

        return super(RegisterFormView, self).form_valid(form)


def _email_message(value):
    message = render_to_string('send_message.txt', {
                               'value': value, })
    return message


def complete_registration(request, value):
    x = value.replace('___', ':')
    decript_string = signing.loads(x)
    user_id = decript_string['id']
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('/login/')


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = "password_change.html"
    success_url = "/blog/"

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = UserLoginForm
    template_name = "login.html"
    success_url = "/blog/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/blog/")


def government(request):
    users = CustomUser.objects.filter(goverment=True)
    data = {'users': users}
    return render_to_response('profile/government.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def password_change(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            redirect('/password_change_done/')

    return render(request, 'password_change.html', {
        'form': form,
    })


def restart_password(request):
    form = RestartPasswordForm()

    errors = []
    if request.method == 'POST':
        form = RestartPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = randstring(6)
                user.set_password(token)
                user.save()
                message = email_message_pass(user.username, token)
                try:
                    send_mail("Сброс пароля на сайте tkr.od.ua",
                              message,
                              'support@tkr.od.ua',
                              [user.email],
                              fail_silently=False)
                    return redirect('/restart_password_done/')
                except BadHeaderError:
                    pass
            except:
                errors.append('Пользователь с данным e-mail - не существует.')

    return render(request, 'password_reset.html', {
        'errors': errors,
        'form': form,
    })


def randstring(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])


def email_message_pass(login, token):
    message = render_to_string('send_message_pass.txt', {
                               'login': login,
                               'pass': token, })
    return message


@login_required
def profile_edit(request):
    profile = CustomUser.objects.get(user=request.user)

    template = 'profile_edit.html'

    if request.POST:    # If the form has been submitted...
        form = CustomUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():     # All validation rules pass
            form.save()
            url = u'/profile/%s' % profile.id
            return redirect(url)
        else:
            return render_to_response(template, {
                                      'form': form,
                                      'profile': profile},
                                      context_instance=RequestContext(request))
    else:
        form = CustomUserForm(
            instance=profile,
            initial={
                'first_name': profile.user.first_name,
                'last_name': profile.user.last_name,
                'email': profile.user.email,
            })
    return render_to_response(template, {
                              'form': form,
                              'profile': profile},
                              context_instance=RequestContext(request))


def profile(request, profile_id):
    profile2 = CustomUser.objects.get(id=profile_id)
    comments = PowerComment.objects.filter(owner=profile2).order_by('-date_creation')[:10]
    materials = Material.objects.filter(owner=profile2).exclude(state=2)

    material_enable = Material.objects.filter(owner=profile2, state=1)
    material_disable = Material.objects.filter(owner=profile2, state=0)

    articles_disable = _get_articles(material_disable)
    articles_enable = _get_articles(material_enable)

    reports_disable = _get_reports(material_disable)
    reports_enable = _get_reports(material_enable)

    data = {'profile2': profile2, 'comments': comments,
            'articles_disable': articles_disable,
            'articles_enable': articles_enable,
            'reports_disable': reports_disable,
            "reports_enable": reports_enable, }
    return render_to_response('profile.html',
                              data,
                              context_instance=RequestContext(request))


def _get_articles(materials):
    articles = []

    for material in materials:
        if material.rank == 1 or material.rank == 3 or material.rank == 4:
            articles.append(material)
        else:
            pass

    return articles


def _get_reports(materials):
    reports = []

    for material in materials:
        if material.rank == 0 or material.rank == 2:
            reports.append(material)
        else:
            pass

    return reports


@login_required
def profile_block(request, profile_id):
    profile = CustomUser.objects.get(user=request.user)

    if not profile.moderator and profile.user.is_superuser:
        return redirect('/login/')

    custom_user = CustomUser.objects.get(id=profile_id)
    if custom_user.user.is_superuser:
        return redirect('/')

    comments = PowerComment.objects.filter(owner=custom_user)
    for comment in comments:
        comment.state = 0
        comment.save()

    custom_user.user.is_active = False
    custom_user.karma = -999
    custom_user.save()

    return redirect('/')
