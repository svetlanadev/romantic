# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.views.generic import ListView, DetailView
from government.models import CustomUser


class GovernmentListView(ListView):
    model = CustomUser
    context_object_name = 'users'
    # Под данным именем наш список статей будет доступен в шаблоне
    template_name = 'government_list.html'


class GovernmentDetailView(DetailView):
    model = CustomUser

    template_name = 'government_detail.html'
