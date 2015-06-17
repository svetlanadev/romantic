# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from materials.forms import MaterialForm, AttachedFilesForm
from materials.models import Material, Dirs
from hike.models import TypeHike, Region, Difficulty
from profile.models import CustomUser


def materials(request, state):
    type_material, name_material = _type_material(state)
    materials = Material.objects.all().filter(state=type_material)
    dirs = Dirs.objects.all().filter(state=type_material)
    data = {'materials': materials, 'dirs': dirs,
            'name_material': name_material}
    return render_to_response('materials/material_list.html',
                              data,
                              context_instance=RequestContext(request))


# def sandbox(request, state):
#     type_material, name_material = _type_material(state)
#     materials = Material.objects.all().filter(state=type_material)
#     data = {'materials': materials, }
#     return render_to_response('materials/sandbox.html',
#                               data,
#                               context_instance=RequestContext(request))


def material_detail(request, material_id):
    material = Material.objects.get(id=material_id)
    data = {'material': material, }
    return render_to_response('materials/material_detail.html',
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


# @login_required
# def sandbox_new(request):
#     profile = CustomUser.objects.get(user=request.user)
#     type_hike = TypeHike.objects.all()
#     region = Region.objects.all()
#     difficulty = Difficulty.objects.all()
#     if request.method == "POST":
#         form = MaterialForm(request.POST)
#         if form.is_valid():
#             material = form.save(owner=profile)
#             material_last = Material.objects.first()
#             url = u'/materials/%s' % material_last.id
#             return redirect(url)
#         else:
#             data = {'form': form, 'type_hikes': type_hike,
#                     'regions': region, 'difficultys': difficulty}
#             return render_to_response('materials/sandbox_new.html',
#                                       data,
#                                       context_instance=RequestContext(request))

#     else:  # GET
#         form = MaterialForm()
#         data = {'form': form, 'type_hikes': type_hike,
#                 'regions': region, 'difficultys': difficulty}
#         return render_to_response('materials/sandbox_new.html',
#                                   data,
#                                   context_instance=RequestContext(request))


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
    type_hike = TypeHike.objects.all()
    region = Region.objects.all()
    difficulty = Difficulty.objects.all()
    type_material, name_material = _type_material(state)

    if request.method == "POST":
        print "==========+POST+++++++++++++++"
        form = MaterialForm(request.POST)
        form_file = AttachedFilesForm(request.POST, request.FILES)
        if form.is_valid():
            print "FORM"
            material = form.save(owner=owner)
            material_last = Material.objects.first()
            url = u'/materials/%s' % material_last.id
            return redirect(url)
        else:
            data = {'form': form, 'form_file': form_file, 'type_hikes': type_hike,
                    'regions': region, 'difficultys': difficulty}
            return render_to_response('materials/material_%s_new.html' % state,
                                      data,
                                      context_instance=RequestContext(request))

    else:  # GET
        form = MaterialForm()
        form_file = AttachedFilesForm()
        data = {'form': form, 'form_file': form_file, 'type_hikes': type_hike,
                'regions': region, 'difficultys': difficulty}
        return render_to_response('materials/material_%s_new.html' % state,
                                  data,
                                  context_instance=RequestContext(request))


@login_required
def material_edit(request, material_id):
    user = CustomUser.objects.get(user=request.user)
    material = Material.objects.get(id=material_id)

    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save(owner=user)
            url = u'/materials/%s' % material_id
            return redirect(url)

    form = MaterialForm(instance=material)
    data = {'form': form, 'material': material}
    return render_to_response('materials/material_edit.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def material_my(request):
    user = CustomUser.objects.get(user=request.user)
    material_enable = Material.objects.filter(owner=user).exclude(state=0)
    material_disable = Material.objects.filter(owner=user, state=0)

    data = {'materials': material_enable, 'material_disable': material_disable}
    return render_to_response('materials/material_my.html',
                              data,
                              context_instance=RequestContext(request))


def _type_material(state):
    if state == 'report':
        type_material = 1
        name_material = "Отчеты походов"
    elif state == 'passport':
        type_material = 3
        name_material = "Паспорта препятствий"
    elif state == 'art':
        type_material = 2
        name_material = "Творчество"
    elif state == 'sandbox':
        type_material = 0
        name_material = "Песочница"
    elif state == 'article':
        type_material = 5
        name_material = "Статья"
    else:
        type_material = 999
        name_material = "errors"
    return type_material, name_material
