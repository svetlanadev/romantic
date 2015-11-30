# coding: utf-8
# author: dlyapun

from django.core.exceptions import ObjectDoesNotExist
from materials.forms import MaterialForm
from materials.models import Material, Dirs
from hike.models import TypeHike, Region, Difficulty


def _type_material(state):
    if state == 'report':
        type_material = 0
        name_material = "Отчеты"
        category_material = 'report'
    elif state == 'art':
        type_material = 1
        name_material = "Творчество"
        category_material = 'article'
    elif state == 'passport':
        type_material = 2
        name_material = "Паспорта препятствий"
        category_material = 'report'
    elif state == 'doc':
        type_material = 3
        name_material = "Документы и МКК"
        category_material = 'article'
    elif state == 'article':
        type_material = 4
        name_material = "Статьи"
        category_material = 'article'
    else:
        type_material = 999
        name_material = "errors"
    return type_material, name_material, category_material


def _get_objects_articles(point):
    articles = []
    materials = Material.objects.filter(state=point, rank=1)

    for material in materials:
        articles.append(material)
    materials = Material.objects.filter(state=point, rank=3)
    for material in materials:
        articles.append(material)
    materials = Material.objects.filter(state=point, rank=4)
    for material in materials:
        articles.append(material)

    return articles


def _get_objects_reports(point):
    reports = []
    materials = Material.objects.filter(state=point, rank=0)

    for material in materials:
        reports.append(material)
    materials = Material.objects.filter(state=point, rank=2)
    for material in materials:
        reports.append(material)
    return reports


def _material_filter(request, materials):
    try:
        difficulty_filter = Difficulty.objects.get(id=request.POST['difficulty'])
    except ObjectDoesNotExist:
        difficulty_filter = 0
    try:
        type_hike_filter = TypeHike.objects.get(id=request.POST['type_hike'])
    except ObjectDoesNotExist:
        type_hike_filter = 0
    try:
        region_filter = Region.objects.get(id=request.POST['region'])
    except ObjectDoesNotExist:
        region_filter = 0

    if type_hike_filter != 0:
        materials = materials.filter(type_hike=type_hike_filter)
    if difficulty_filter != 0:
        materials = materials.filter(difficulty=difficulty_filter)
    if region_filter != 0:
        materials = materials.filter(region=region_filter)

    return materials
