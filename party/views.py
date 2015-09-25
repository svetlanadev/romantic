# coding: utf-8
# author: dlyapun

from django.views.generic import ListView, DetailView
from party.models import Party
from profile.models import CustomUser
from party.forms import PartyForm
from django.contrib.auth.decorators import login_required
from force_blog.models import Category
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from datetime import datetime


class PartyListView(ListView):
    model = Party

    context_object_name = 'partys'

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            qs = Party.objects.prefetch_related('category').filter(date_start__gt=datetime.now()).exclude(state=0)
            return qs
        else:
            profile = CustomUser.objects.get(user=self.request.user)
        if profile.moderator or profile.goverment or profile.user.is_superuser:
            qs = Party.objects.prefetch_related('category').filter(date_start__gt=datetime.now())
        else:
            qs = Party.objects.prefetch_related('category').filter(date_start__gt=datetime.now()).exclude(state=0)
        return qs

    def get_context_data(self, **kwargs):
        context = super(PartyListView, self).get_context_data(**kwargs)
        return context


class PartyDetailView(DetailView):
    model = Party


class PartyPostListViewTag(PartyListView):

    def get_queryset(self, **kwargs):
        category = self.kwargs['category_id']
        return super(PartyPostListViewTag, self).get_queryset().filter(category=category)


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