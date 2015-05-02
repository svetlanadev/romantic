# coding: utf-8

from django import template
from django.core import urlresolvers
from django.core.urlresolvers import reverse, NoReverseMatch
from power_comments.forms import PowerCommentForm
from power_comments.models import PowerComment


register = template.Library()


@register.inclusion_tag('power_comments/comments.html')
def power_comments(request, app_url):
    comments = PowerComment.objects.all().filter(app=app_url, state=1)
    count_comments = comments
    data = {'comments': comments,
            'app_url': app_url,
            'count_comments': count_comments,
            'request': request}
    return data


@register.simple_tag()
def count_power_comments(app_url):
    comments = PowerComment.objects.all().filter(app=app_url, state=1)
    count_power_comments = comments.count()
    return count_power_comments


@register.simple_tag()
def url_with_comment(app_url):
    id_content = ''.join(filter(lambda x: x.isdigit(), app_url))
    if "blog" in app_url:
        from force_blog.models import BlogPost
        obj = BlogPost.objects.get(id=id_content)
        url = obj.title
    elif "materials" in app_url:
        from materials.models import Material
        obj = Material.objects.get(id=id_content)
        url = obj.title
    elif "party" in app_url:
        from party.models import Party
        obj = Party.objects.get(id=id_content)
        url = obj.name
    return url


@register.simple_tag()
def power_url_edit(obj):
    url = urlresolvers.reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                                       obj._meta.module_name),
                                                       args=[obj.id])
    return url
