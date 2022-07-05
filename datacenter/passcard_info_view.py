from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timedelta


def get_duration(visit):
    delta = localtime() - localtime(visit.entered_at)
    if visit.leaved_at:
        delta = localtime(visit.leaved_at) - localtime(visit.entered_at)
    delta -= timedelta(microseconds=delta.microseconds)
    return delta


def format_duration(duration):
    return f"{int(duration.total_seconds()) // 3600}:{int(duration.total_seconds()) % 3600 // 60}"


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    print(passcard.owner_name, len(visits))  # вывод в консоль
    this_passcard_visits = []
    for v in visits:
        vis = {
            'entered_at': v.entered_at,
            'duration': format_duration(get_duration(v)),
            'is_strange': v.is_long()
        }
        this_passcard_visits.append(vis)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
