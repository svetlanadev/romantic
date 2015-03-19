# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from materials.forms import MaterialForm
from materials.models import Material, Dirs
from hike.models import TypeHike, Region, Difficulty
from profile.models import CustomUser


def material_report(request):
    type_material = 1 # HIKE
    materials = Material.objects.all().filter(state=type_material)
    dirs = Dirs.objects.all()
    data = {'materials': materials, 'dirs': dirs,}
    return render_to_response('materials/material_list.html',
                              data,
                              context_instance=RequestContext(request))


def material_passport(request):
    type_material = 3 # HIKE
    materials = Material.objects.all().filter(state=type_material)
    dirs = Dirs.objects.all()
    data = {'materials': materials, 'dirs': dirs,}
    return render_to_response('materials/material_list.html',
                              data,
                              context_instance=RequestContext(request))


def material_art(request):
    type_material = 2 # HIKE
    materials = Material.objects.all().filter(state=type_material)
    dirs = Dirs.objects.all()
    data = {'materials': materials, 'dirs': dirs,}
    return render_to_response('materials/material_list.html',
                              data,
                              context_instance=RequestContext(request))


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


@login_required
def material_new(request):
    owner = CustomUser.objects.get(user=request.user)
    print owner
    type_hike = TypeHike.objects.all()
    region = Region.objects.all()
    difficulty = Difficulty.objects.all()
    if request.method == "POST":
        form = MaterialForm(request.POST)
        print form.errors
        if form.is_valid():
            material = form.save(owner=owner)
            material_last = Material.objects.first()
            print material_last.title
            new_dir = text = form.cleaned_data['new_dirs']
            dirs = Dirs(dir_name=new_dir)
            dirs.materials.add(material_last)
            dirs.save()
            print dirs
            
            url = u'/material/%s' % material_last.id
            return redirect(url)
        else:
            data = {'form': form, 'type_hikes': type_hike, 'regions': region, 'difficultys': difficulty}
            return render_to_response('materials/material_new.html',
                                      data,
                                      context_instance=RequestContext(request))

    else: # GET 
        form = MaterialForm()
        data = {'form': form, 'type_hikes': type_hike, 'regions': region, 'difficultys': difficulty}
        return render_to_response('materials/material_new.html',
                                  data,
                                  context_instance=RequestContext(request))
