# coding=utf-8

from party.models import Party
from django.core.exceptions import ObjectDoesNotExist


def contex_party(request):
    try:
        calendar = Party.objects.all()
    except ObjectDoesNotExist:
        calendar = "ERROR"

    return {'calendar': calendar}
