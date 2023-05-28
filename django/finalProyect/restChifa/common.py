from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import datetime
from django.conf import settings
from django.core.paginator import Paginator




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