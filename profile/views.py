# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from profile.models import CustomUser


class ProfileListView(ListView):
    model = CustomUser
    context_object_name = 'users'
    # Под данным именем наш список статей будет доступен в шаблоне


class ProfileDetailView(DetailView):
    model = CustomUser

    context_object_name = 'profile'


def government(request):
    users = CustomUser.objects.filter(goverment=True)
    data = {'users': users}
    return render_to_response('profile/government.html',
                              data,
                              context_instance=RequestContext(request))