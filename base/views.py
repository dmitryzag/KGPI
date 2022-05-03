from calendar import weekday
from django.shortcuts import render
from .models import Faculty, Schedule, Speciality, Group, WeekParity


# Create your views here.


def hello(req):
    return render(req, 'main.html')


def faculties(req):
    faculties = Faculty.objects.all()
    context = {'faculties': faculties}
    return render(req, 'base/faculties.html', context)


def specialities(req, facul):
    specialities = Speciality.objects.filter(faculty__slug=facul)
    items = Faculty.objects.get(slug=facul)
    context = {'specialities': specialities, 'items': items}
    print(facul)
    return render(req, 'base/specialities.html', context)


def groups(req, facul, special):
    groups = Group.objects.filter(speciality__slug=special)
    speciality = Speciality.objects.get(slug=special)
    faculty = Faculty.objects.get(slug=facul)
    items = [faculty, speciality]
    context = {'groups': groups, 'items': items}

    return render(req, 'base/groups.html', context)


def schedule(req, facul, special, group):

    schedules = Schedule.objects.filter(parity=1)
    weeks = WeekParity.objects.all()
    count = 0
    weekdays = []

    for week in weeks:
        week = {'week': Schedule.objects.filter(parity=week)}
        weekdays.append(week)

    speciality = Speciality.objects.get(slug=special)
    faculty = Faculty.objects.get(slug=facul)
    groups = Group.objects.get(slug=group)

    items = [faculty, speciality, groups]
    context = {'schedules': schedules,
               'items': items, 'weekdays': weekdays, 'count': count}
    print(schedules)
    return render(req, 'base/schedule.html', context)
