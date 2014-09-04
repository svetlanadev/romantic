# coding: utf-8

# from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from profile.models import CustomUser
from django.shortcuts import render_to_response, redirect, render
from power_comments.models import PowerComment
from power_comments.forms import PowerCommentForm


@login_required
def new_power_comment(request):
    owner = CustomUser.objects.get(user=request.user)
    if request.method == "POST":
        id_app = request.POST['id_app']
        form = PowerCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = PowerComment(text=text,
                                   app=id_app,
                                   owner=owner)
            comment.save()
            return redirect('%s' % id_app)
        else:
            data = {'form': form}
            return render('force_blog/blogpost_list.html',
                          data)

    else:
        return redirect('/')


@login_required
def karma_power_comments(request):
    if request.method == "POST":
        id_app = request.POST['id_app']
    return redirect('/')
