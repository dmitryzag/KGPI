from .models import Faculty, Schedule, Speciality, Group, WeekParity, DayOfWeek
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count


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
    schedule = Schedule.objects.values(
        'parity').distinct().aggregate(parity=Count('parity'))
    a = []

    for i in range(1, schedule.get('parity') + 1):
        a.append(Schedule.objects.filter(parity=i, group__slug=group))

    # weeks = DayOfWeek.objects.all()

    weekdays = []

    # for week in weeks:
    #     week = {'week': Schedule.objects.filter(
    #         day=week, group__slug=group, parity=1)}
    #     weekdays.append(week)

    for i in range(1, schedule.get('parity') + 1):
        b = []
        weeks = DayOfWeek.objects.all()
        print(i, weeks)
        for week in weeks:
            week = {'week': Schedule.objects.filter(
                day=week, group__slug=group, parity=i)}
            b.append(week)
        weekdays.append(b)
        b = []

    speciality = Speciality.objects.get(slug=special)
    faculty = Faculty.objects.get(slug=facul)
    groups = Group.objects.get(slug=group)
    items = [faculty, speciality, groups]

    paginator = Paginator(weekdays, 1)
    page_number = req.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {'items': items, 'weekdays': weekdays, 'page_obj': page_obj}

    return render(req, 'base/schedule.html', context)
