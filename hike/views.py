# coding: utf-8
# author: dlyapun

from django.views.generic import ListView
from hike.models import Hike


class HikeListView(ListView):
    model = Hike
    # Под данным именем наш список статей будет доступен в шаблоне
    context_object_name = 'hikes'
    # Количество объектов на 1 страницу
    paginate_by = 3