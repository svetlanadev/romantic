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
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist


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
        pass
    else:
        if request.method == "POST":
            id_comment = request.POST['id_comment']
            disable = request.POST['disable']
            comment = PowerComment.objects.get(id=id_comment)
            if disable == "true":
                comment.state = 0 # DISABLE
                comment.save()
        else: 
            return redirect('/')            
        return redirect(comment.app)

# <django.db.models.fields.related.ManyRelatedManager object at 0x7f50182ede90>

def ajax_test(request):
    results = {'success':False}

    if request.is_ajax():
        print request.POST
    # Тут — потрібні нам алгоритми
    if request.is_ajax():
        results = {'success':True, 'param1':'Good', 'param2':randint(0,40)}

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')


def ajax_karma_minus(request):
    user = CustomUser.objects.get(user=request.user)
    results = {'success':False}
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
    else:
        message = "Недостаточно кармы для голосования"

    if request.is_ajax():
        results = {'success':True, 'rating':comment.rating, 'id_comment':comment.id, 'message':message, }
        json = simplejson.dumps(results)
        return HttpResponse(json, mimetype='application/json')

    url = comment.app
    return redirect(url)


def ajax_karma_plus(request):
    user = CustomUser.objects.get(user=request.user)
    results = {'success':False}
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
    else:
        message = "Недостаточно кармы для голосования"

    if request.is_ajax():
        results = {'success':True, 'rating':comment.rating, 'id_comment':comment.id, 'message':message, }
        json = simplejson.dumps(results)
        return HttpResponse(json, mimetype='application/json')

    url = comment.app
    return redirect(url)


@login_required
def new_power_comment(request):
    owner = CustomUser.objects.get(user=request.user)
    results = {'success': False }

    if request.is_ajax():
        form = PowerCommentForm(request.POST)
        text = request.POST['text']
        if form.is_valid():
            id_app = request.POST['id_app']
            id_last_comment = request.POST['id_last_comment']

            if id_last_comment != '0':
                pre_comment = PowerComment.objects.get(id=id_last_comment)
                # print "PRE COMMENT: %s" % pre_comment
                try:
                    last_comment = PowerComment.objects.filter(pre_comment=id_last_comment).last()
                    # print "LAST COMMENT: %s" % last_comment
                    if last_comment == None:
                        position = pre_comment.position + 1

                    else:
                        position = last_comment.position + 1

                except ObjectDoesNotExist:
                    position = pre_comment.position + 1

                if pre_comment.count_inc:
                    count_inc = pre_comment.count_inc + 1
                else:
                    count_inc = 1

                # print "POSITION: %s" % position

                all_comments = PowerComment.objects.filter(app=id_app)

                for comment in all_comments:
                    # print "COMMENT: %s" % comment
                    if comment.position >= position:
                        comment.position += 1
                        comment.save()

                comment = PowerComment(text=text, app=id_app, owner=owner, position=position, pre_comment=pre_comment.id, count_inc=count_inc)
                comment.save()

            ############################################################################
            else:
                try:
                    last_comment = PowerComment.objects.filter(app=id_app).last()
                    if last_comment == None:
                        position = 1
                    else:
                        position = last_comment.position + 1
                except ObjectDoesNotExist:
                    position = 1

                comment = PowerComment(text=text,
                                       app=id_app,
                                       owner=owner,
                                       position=position)
                comment.save()

            comments = PowerComment.objects.all().filter(app=id_app, state=1)
            new_comment = PowerComment.objects.last()
            return render_to_response('power_comments/new_comment.html', { 
                                      'comments': comments },
                                      context_instance=RequestContext(request))

        else:
            results = {'success':False, 'message': 'Максимум 1000 символов', 'text': text}

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')
