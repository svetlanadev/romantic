# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.views.generic import ListView, DetailView
from profile.models import CustomUser


class ProfileListView(ListView):
    model = CustomUser
    context_object_name = 'users'
    # Под данным именем наш список статей будет доступен в шаблоне
    template_name = 'profile_list.html'


class ProfileDetailView(DetailView):
    model = CustomUser

    template_name = 'profile_detail.html'
