from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import datetime



def get_datetime_operation_add(date_utc_user, days, seconds):
    result = date_utc_user
    result += timedelta(days,seconds)
    return result
