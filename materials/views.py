# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from materials.forms import MaterialForm, AttachedFilesForm
from materials.models import Material, Dirs
from hike.models import TypeHike, Region, Difficulty
from force_blog.models import Category
from profile.models import CustomUser


ENABLE = 1
DISABLE = 0


def materials(request, state):
    type_material, name_material, name_material_many, category_material = _type_material(state)
    type_hike = TypeHike.objects.all()
    region = Region.objects.all()
    difficulty = Difficulty.objects.all()
    categorys = Category.objects.all()

    if request.method == "POST":
        materials = Material.objects.filter(rank=type_material, state=ENABLE)
        materials = _material_filter(request, materials)
    else:
        materials = Material.objects.filter(rank=type_material, state=ENABLE)[:10]

    dirs = Dirs.objects.all().filter(state=type_material)

    data = {'materials': materials, 
            'dirs': dirs,
            'type_hikes': type_hike,
            'regions': region, 
            'difficultys': difficulty,
            'name_material': name_material,
            'name_material_many': name_material_many,
            'categorys': categorys}
    return render_to_response('materials/%s/material_list.html' % category_material,
                              data,
                              context_instance=RequestContext(request))


def material_detail(request, material_id):
    material = Material.objects.get(id=material_id)

    if material.state == DISABLE:
        try:
            profile = CustomUser.objects.get(user=request.user)
            if profile.moderator or profile.user.is_superuser or material.owner == profile:
                category_material = material.get_type_material()
                data = {'material': material, }
                return render_to_response('materials/%s/material_detail.html' % category_material,
                                          data,
                                          context_instance=RequestContext(request))
            else:
                return redirect('/party/')
        except:
            return redirect('/')

    else:
        category_material = material.get_type_material()
        data = {'material': material, }
        return render_to_response('materials/%s/material_detail.html' % category_material,
                                  data,
                                  context_instance=RequestContext(request))


def material_folder(request, dir_id):
    one_dir = Dirs.objects.get(id=dir_id)
    data = {'one_dir': one_dir, }
    return render_to_response('materials/material_dir.html',
                              data,
                              context_instance=RequestContext(request))


def library(request):
    data = {'one_dir': 'one_dir', }
    return render_to_response('materials/library.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def material_page(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    data = {'type_hikes': 'type_hike'}
    return render_to_response('materials/material_new.html',
                              data,
                              context_instance=RequestContext(request))

@login_required
def material_new(request, state):
    if not request.user.is_authenticated():
        return redirect('/login/')

    owner = CustomUser.objects.get(user=request.user)

    if state == 'doc':
        if not owner.moderator and owner.user.is_superuser:
            return redirect('/login/')


    type_hike = TypeHike.objects.all()
    region = Region.objects.all()
    difficulty = Difficulty.objects.all()
    type_material, name_material, name_material_many, category_material = _type_material(state)
    categorys = Category.objects.all()

    if request.method == "POST":
        form = MaterialForm(request.POST)
        form_file = AttachedFilesForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                tags = form.cleaned_data['category']
            except KeyError:
                new_tag = Category.objects.create(category=request.POST['category'])
            # tags = form.cleaned_data['category']
            material = form.save_with_owner(owner=owner)
            material_last = Material.objects.first()
            for x in tags:
                tag = Category.objects.get(category=x)
                material.category.add(tag)

            url = u'/materials/%s' % material_last.id
            return redirect(url)
        else:
            data = {'form': form, 'form_file': form_file, 'type_hikes': type_hike,
                    'regions': region, 'difficultys': difficulty,
                    'category_material': category_material,
                    'name_material': name_material,
                    'name_material_many': name_material_many,
                    'type_material': type_material,
                    'categorys': categorys}
            return render_to_response('materials/%s/material_new.html' % category_material,
                                      data,
                                      context_instance=RequestContext(request))

    else:  # GET
        form = MaterialForm()
        form_file = AttachedFilesForm()
        data = {'form': form, 'form_file': form_file, 'type_hikes': type_hike,
                'regions': region, 'difficultys': difficulty,
                'category_material': category_material,
                'name_material': name_material,
                'name_material_many': name_material_many,
                'type_material': type_material,
                'categorys': categorys}
        return render_to_response('materials/%s/material_new.html' % category_material,
                                  data,
                                  context_instance=RequestContext(request))


@login_required
def material_edit(request, material_id):
    profile = CustomUser.objects.get(user=request.user)
    material = Material.objects.get(id=material_id)

    if not profile.moderator and profile.user.is_superuser and material.owner == profile:
        return redirect('/login/')

    if material.state == ENABLE:
        if profile.moderator and profile.user.is_superuser:
            pass
        else:
            url = u'/materials/%s' % material_id
            return redirect(url)

    categorys = Category.objects.all()
    type_hike = TypeHike.objects.all()
    region = Region.objects.all()
    difficulty = Difficulty.objects.all()

    category_material = material.get_type_material()
    # type_material, name_material, category_material2 = _type_material(state)

    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        form.is_valid()
        
        
        if form.is_valid():
            try:
                tags = form.cleaned_data['category']
            except KeyError:
                new_tag = Category.objects.create(category=request.POST['category'])

            for x in categorys:
                material.category.remove(x)

            for x in tags:
                try:
                    tag = Category.objects.get(category=x)
                except ObjectDoesNotExist:
                    pass
                
                try:
                    material.category.add(tag)
                except TypeError:
                    pass

            form.save()
            url = u'/materials/%s' % material_id
            return redirect(url)

    else:
        form = MaterialForm(instance=material)

    data = {'form': form, 'material': material, 
            'categorys': categorys, 
            'type_hikes': type_hike,
            'regions': region, 
            'difficultys': difficulty,}
    return render_to_response('materials/%s/material_edit.html' % category_material,
                              data,
                              context_instance=RequestContext(request))


@login_required
def material_hidden(request, material_id):
    profile = CustomUser.objects.get(user=request.user)
    if not profile.moderator and profile.user.is_superuser:
        return redirect('/login/')

    material = Material.objects.get(id=material_id)
    if material.state == ENABLE:
        material.state = DISABLE # DISABLE
        material.save()
    else:
        material.state = ENABLE # ENABLE
        material.save()

    url = u'/materials/%s' % material_id
    return redirect(url)


@login_required
def sandbox(request):
    profile = CustomUser.objects.get(user=request.user)

    if not profile.moderator and profile.goverment and profile.user.is_superuser:
        return redirect('/login/')

    articles = _get_objects_articles(DISABLE)
    reports = _get_objects_reports(DISABLE)
    print reports

    data = {'articles': articles, 'reports': reports}
    return render_to_response('materials/sandbox.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def material_my(request):
    user = CustomUser.objects.get(user=request.user)
    material_enable = Material.objects.filter(owner=user, state=1)
    material_disable = Material.objects.filter(owner=user, state=0)

    data = {'materials': material_enable, 'material_disable': material_disable}
    return render_to_response('materials/material_my.html',
                              data,
                              context_instance=RequestContext(request))


def _type_material(state):
    if state == 'report':
        type_material = 0
        name_material = "Отчет"
        name_material_many = 'Отчеты'
        category_material = 'report'
    elif state == 'art':
        type_material = 1
        name_material = "Творчество"
        name_material_many = "Творчество"
        category_material = 'article'
    elif state == 'passport':
        type_material = 2
        name_material = "Паспорт препятствия"
        name_material_many = "Паспорта препятствий"
        category_material = 'report'
    elif state == 'doc':
        type_material = 3
        name_material = "Документы и МКК"
        name_material_many = "Документы и МКК"
        category_material = 'article'
    elif state == 'article':
        type_material = 4
        name_material = "Статья"
        name_material_many = "Статьи"
        category_material = 'article'
    else:
        type_material = 999
        name_material = "errors"
        name_material_many = "errors"
        category_material = 'article'
    return type_material, name_material, name_material_many, category_material


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
