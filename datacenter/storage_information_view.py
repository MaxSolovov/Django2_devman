from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration

def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    serializad_nonclosed_visits = []
    for data_visit in non_closed_visits:
        one_person_visit = {
            'who_entered': data_visit.passcard.owner_name,
            'entered_at': data_visit.entered_at,
            'duration': format_duration(get_duration(data_visit)),
        }
        serializad_nonclosed_visits.append(one_person_visit)

    context = {
        'non_closed_visits': serializad_nonclosed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
