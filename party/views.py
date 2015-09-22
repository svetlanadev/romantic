# coding: utf-8
# author: dlyapun

from django.views.generic import ListView, DetailView
from party.models import Party
from profile.models import CustomUser
from party.forms import PartyForm
from django.contrib.auth.decorators import login_required
from force_blog.models import BlogPost, BlogEdit, Category
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext


class PartyListView(ListView):
    model = Party

    context_object_name = 'partys'


class PartyDetailView(DetailView):
    model = Party

@login_required
def party_new(request):
    profile = CustomUser.objects.get(user=request.user)
    categorys = Category.objects.all()
    form = PartyForm()

    if not profile.moderator and profile.goverment and profile.user.is_superuser:
        return redirect('/login/')

    if request.method == "POST":
        form = PartyForm(request.POST)

        if form.is_valid():
            try:
                tags = form.cleaned_data['category']
            except KeyError:
                new_tag = Category.objects.create(category=request.POST['category'])
            
            # tags = form.cleaned_data['category']
            form.save_with_owner(owner=profile)
            form.save()
            party = Party.objects.first()
            for x in tags:
                tag = Category.objects.get(category=x)
                party.category.add(tag)

            url = u'/party/%s' % party.id
            return redirect(url)

    data = {'form': form, 'categorys': categorys}
    return render_to_response('party/party_new.html',
                              data,
                              context_instance=RequestContext(request))