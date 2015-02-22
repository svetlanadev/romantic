# coding: utf-8

import json

# from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from profile.models import CustomUser
from django.shortcuts import render_to_response, redirect, render
from power_comments.models import PowerComment
from power_comments.forms import PowerCommentForm
from django.utils import simplejson
from django.http import HttpResponse
from random import randint


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

def ajax_test(request):
    results = {'success':False}

    if request.is_ajax():
        print request.POST
    # Тут — потрібні нам алгоритми
    if True:
        results = {'success':True, 'param1':'Good', 'param2':randint(0,40)}

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')


def ajax_karma_minus(request):
    user = CustomUser.objects.get(user=request.user)
    results = {'success':False}

    # Тут — потрібні нам алгоритми
    if request.is_ajax():
        id_comment = request.POST['id_comment']
        comment = PowerComment.objects.get(id=id_comment)
        message = ""
        if user.karma > -10:
            if user not in comment.karma_users.all():
                comment.rating = comment.rating - 1
                user.karma = user.karma - 1
                comment.save()
                user.save()
                comment.karma_users.add(user)
                message = "Ваш голос учтен"
            else:
                message = "Вы уже поставили рейтинг"
                print message
        else:
            message = "Недостаточно кармы для комментирования"
            print message

        results = {'success':True, 'rating':comment.rating, 'id_comment':comment.id, 'message':message, }
        

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')


def ajax_karma_plus(request):
    user = CustomUser.objects.get(user=request.user)
    results = {'success':False}
    print user

    # Тут — потрібні нам алгоритми
    if request.is_ajax():
        id_comment = request.POST['id_comment']
        comment = PowerComment.objects.get(id=id_comment)
        message = ""
        if user.karma > -10:
            if user not in comment.karma_users.all():
                comment.rating = comment.rating + 1
                user.karma = user.karma + 1
                comment.save()
                user.save()
                comment.karma_users.add(user)
                message = "Ваш голос учтен"
            else:
                message = "Вы уже поставили рейтинг"
                print message
        else:
            message = "Недостаточно кармы для комментирования"
            print message

        results = {'success':True, 'rating':comment.rating, 'id_comment':comment.id, 'message':message, }
        

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')