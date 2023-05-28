from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import datetime
from django.conf import settings
from django.core.paginator import Paginator
import pytz




class Common:

    def get_datetime_operation_add(date_utc_user, days, seconds):
        result = date_utc_user
        result += timedelta(days,seconds)
        return result

    def is_valid_date_reserve(date_utc):
        return date_utc > Common.get_limit_less_date_reserve() and date_utc < Common.get_limit_more_date_reserve()

    def get_limit_less_date_reserve():
        return Common.get_datetime_operation_add(timezone.now(), settings.DAYS_IN_ADVANCE_RESERVES, settings.SECONDS_IN_ADVANCE_RESERVES)

    def get_limit_more_date_reserve():
        return Common.get_datetime_operation_add(timezone.now(), settings.LIMIT_DAYS_IN_ADVANCE_RESERVES, settings.LIMIT_SECONDS_IN_ADVANCE_RESERVES)

    def get_paginator(request, model, per_page=settings.PAGINATOR_PER_PAGE):
        if request is None or model is None:
            return False

        return Paginator(model, per_page).get_page(request.GET.get("page"))

    def get_date_utc_from_date_local_javascript(date_local_javascript):
        try:
            bool(datetime.datetime.strptime(date_local_javascript, "%Y-%m-%dT%H:%M"))
            # parse input datetime-local to object datetime format
            date_processing = date_local_javascript.replace('T', '-').replace(':', '-').split('-')
            date_processing = [int(v) for v in date_processing]
            date_local = datetime.datetime(*date_processing)

            #time_zone = pytz.timezone(timezone.get_current_timezone_name())
            #time_zone = pytz.timezone('Europe/Madrid')
            time_zone = pytz.timezone(settings.TIME_ZONE_USER)

            date_time = date_local
            # make time zone aware
            date_local = time_zone.localize(date_time)

            # convert to UTC
            date_utc = date_local.astimezone(pytz.utc)
        except ValueError:
            date_utc = ""

        return date_utc