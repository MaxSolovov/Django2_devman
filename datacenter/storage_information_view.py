from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timedelta


def get_duration(visit):
    delta = localtime() - localtime(visit.entered_at)
    delta -= timedelta(microseconds=delta.microseconds)
    return delta


def format_duration(duration):
    return f"{int(duration.total_seconds()) // 3600}:{int(duration.total_seconds()) % 3600 // 60}"


def storage_information_view(request):
    non_cls_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for v in non_cls_visits:
        n_c_v = {
            'who_entered': v.passcard.owner_name,
            'entered_at': v.entered_at,
            'duration': format_duration(get_duration(v)),
        }
        non_closed_visits.append(n_c_v)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
