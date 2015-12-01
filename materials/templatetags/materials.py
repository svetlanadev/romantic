# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers

register = template.Library()


@register.simple_tag()
def get_material_type(rank):
    if rank == 0:
        name_material = "report"
    elif rank == 1:
        name_material = "art"
    elif rank == 2:
        name_material = "passport"
    elif rank == 3:
        name_material = "doc"
    elif rank == 4:
        name_material = "article"
    else:
        name_material = "get_material_type - ERROR"
    return name_material


@register.simple_tag()
def get_material_type_ru(rank):
        if rank == 0:
            name_material = "Отчеты походов"
        elif rank == 1:
            name_material = "Творчество"
        elif rank == 2:
            name_material = "Паспорта препятствий"
        elif rank == 3:
            name_material = "Документы, МКК"
        elif rank == 4:
            name_material = "Статьи"
        else:
            name_material = "get_material_type_ru - ERROR"
        return name_material