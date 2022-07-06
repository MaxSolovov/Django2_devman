from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    serialized_visits = []
    for data_visit in visits:
        one_person_visit = {
            'entered_at': data_visit.entered_at,
            'duration': format_duration(get_duration(data_visit)),
            'is_strange': data_visit.is_long()
        }
        serialized_visits.append(one_person_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
