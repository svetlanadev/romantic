# coding=utf-8

from profile.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist


def contex_profile(request):

    if request.user.is_authenticated():
        try:
            profile = CustomUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = request.user
    else:
        profile = ""

    return {'profile': profile}
