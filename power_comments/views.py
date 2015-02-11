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
    user = CustomUser.objects.get(user=request.user)
    if request.method == "POST":
        if user.karma < -10:
            message = "Недостаточно кармы для комментирования"
            pass
        id_comment = request.POST['id_comment']
        karma = request.POST['karma']
        comment = PowerComment.objects.get(id=id_comment)
        if user in comment.karma_users.all():
            message = "Вы уже поставили рейтинг"
        else:
            if karma == "minus":
                comment.rating = comment.rating - 1
                user.karma = user.karma - 1
            if karma == "plus":
                comment.rating = comment.rating + 1
                user.karma = user.karma + 1
            comment.save()
            user.save()
            comment.karma_users.add(user)
    else: 
        return redirect('/')            
    return redirect(comment.app)


@login_required
def disable_power_comments(request):
    user = CustomUser.objects.get(user=request.user)
    if not user:
        print "SUKA"
    else:
        print "FUCCCKKING EEYY"
        if request.method == "POST":
            id_comment = request.POST['id_comment']
            disable = request.POST['disable']
            comment = PowerComment.objects.get(id=id_comment)
            print disable
            if disable == "true":
                comment.state = 0 # DISABLE
                comment.save()
                print comment.state
        else: 
            return redirect('/')            
        return redirect(comment.app)

# <django.db.models.fields.related.ManyRelatedManager object at 0x7f50182ede90>
