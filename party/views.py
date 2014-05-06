# coding: utf-8
# author: dlyapun

from django.views.generic import ListView, DetailView
from party.models import Party


class PartyListView(ListView):
    model = Party

    context_object_name = 'partys'


class PartyDetailView(DetailView):
    model = Party
