# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.views.generic import ListView, DetailView
from hike.models import Hike


class HikeListView(ListView):
    model = Hike
    # Под данным именем наш список статей будет доступен в шаблоне
    context_object_name = 'hikes'
    # Количество объектов на 1 страницу
    paginate_by = 3


class HikeDetailView(DetailView):
    model = Hike

    # def get_context_data(self, **kwargs):
    #     context = super(HikeDetailView, self).get_context_data(**kwargs)
    #     context['hike'] = Hike.objects.get(id=self.object.id)
    #     return context

    # def get(self, request, **kwargs):
    #     return self.render_to_response(self.get_context_data(), **kwargs)
