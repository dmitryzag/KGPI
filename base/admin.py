from django.contrib import admin
from .models import Subject, Teacher, Speciality, Faculty, Building, Time, Group, Auditory, Schedule, DayOfWeek, WeekParity
# Register your models here.
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Speciality)
admin.site.register(Faculty)
admin.site.register(Building)
admin.site.register(Time)
admin.site.register(Group)
admin.site.register(Auditory)
admin.site.register(Schedule)
admin.site.register(DayOfWeek)
admin.site.register(WeekParity)
