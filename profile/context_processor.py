# coding=utf-8

from profile.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from power_comments.models import PowerComment


def contex_profile(request):

    last_comments = PowerComment.objects.exclude(state=0)[:10]
    data = {'last_comments': last_comments}

    if request.user.is_authenticated():
        try:
            profile = CustomUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = request.user
    else:
        profile = ""

    return {'profile': profile,
            'last_comments': last_comments,
            }
