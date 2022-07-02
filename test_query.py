import os
import django
from django.utils.timezone import localtime
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

def get_duration(visit):
    delta = localtime() - localtime(visit.entered_at)
    delta -= timedelta(microseconds=delta.microseconds)
    return delta

def format_duration(duration):
    return f"{int(duration.total_seconds())//3600}:{int(duration.total_seconds())%3600//60}"

def is_visit_long(visit, minutes=60):
    if visit.leaved_at:
        delta = localtime(visit.leaved_at) - localtime(visit.entered_at)
        delta -= timedelta(microseconds=delta.microseconds)
        return int(delta.total_seconds())//60 > minutes
    return False

if __name__ == '__main__':
    # Программируем здесь
    #print('Количество пропусков:', Passcard.objects.count(), "\n")  # noqa: T001
    passcards = Passcard.objects.all()
    visits = Visit.objects.all()
    #not_lived = Visit.objects.filter(leaved_at=None)
    #print(not_lived)
    #print(localtime())
    # for v in not_lived:
    #     print(f"{v.passcard.owner_name}")
    #     print(f"Зашёл в хранилище, время по Москве: \n{localtime(v.entered_at)}")
    #     print(f"Находится в хранилище: \n{get_duration(v)} {format_duration(get_duration(v))}\n")

    #long_enter = Visit.objects.filter()
    #print(long_enter)

    # print(*passcards, sep="\n")

    some_person = passcards[9]
    person_visit = Visit.objects.filter(passcard=some_person)
    print(person_visit)
    print(len(person_visit))

    # duration = 1000
    # long_enter = list(filter(lambda v: v.is_long(duration), visits))
    # print(f"Визиты больше {duration} минут:") # , long_enter
    # print(len(long_enter))


