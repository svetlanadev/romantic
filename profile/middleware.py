# coding=utf-8

from django.conf import settings
from django.contrib import auth
from datetime import datetime, timedelta
import time


class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated():
            #  Can't log out if not logged in
            return

        try:
            last_touch = request.session['last_touch']
        except KeyError:
            request.session['last_touch'] = time.time()
            last_touch = request.session['last_touch']

        now_time = int(time.time())

        if now_time - 25500 > int(last_touch):
            auth.logout(request)
            try:
                del request.session['last_touch']
            except KeyError:
                pass
            return
