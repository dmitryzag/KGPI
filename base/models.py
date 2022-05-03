from ctypes import addressof
import email
from pyexpat import model
from statistics import mode
from turtle import position
from django.db import models
from datetime import datetime


# Create your models here.


class Subject(models.Model):
    subject = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    surname = models.TextField(null=True)
    patronymic = models.TextField(null=True)
    slug = models.SlugField(null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='media/', null=True)
    position = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0} {1}.{2}.".format(self.surname, self.firstname[0], self.patronymic[0])


class Faculty(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return "{0}/".format(self.slug)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return "{0}".format(self.slug)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.short_name)


class Building(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    enclosure = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{0}, {1}".format(self.address, self.enclosure)


class Time(models.Model):
    begin = models.TimeField(null=True, blank=True)
    ending = models.TimeField(null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.begin.strftime("%H:%M"), self.ending.strftime("%H:%M"))


class Group(models.Model):
    speciality = models.ForeignKey(
        Speciality, on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)
    num = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return "{0}/".format(self.slug)

    def __str__(self):
        return '{0}-{1}-{2}, {3}'.format(self.speciality.short_name, self.year, self.num, self.faculty.short_name)


class Auditory(models.Model):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    num_auditory = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{0}, ауд: {1}, этаж {2}'.format(self.building, self.num_auditory, self.floor)


class DayOfWeek(models.Model):
    week = models.DateField()

    def __str__(self):
        return '{0}'.format(self.week)


class WeekParity(models.Model):
    parity = models.TextField()

    def __str__(self):
        return "{0}".format(self.parity)


class Schedule(models.Model):
    id_name = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(
        Time, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True, blank=True)
    lesson_type = models.CharField(max_length=200, null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True)
    auditory = models.ForeignKey(
        Auditory, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    day = models.ForeignKey(
        DayOfWeek, on_delete=models.CASCADE, null=True, blank=True, related_name='subj')
    parity = models.ForeignKey(
        WeekParity, on_delete=models.CASCADE, null=True, blank=True, related_name="weekday")

    class Meta:
        ordering = ('lesson',)

    def __str__(self):
        return self.slug


# class Day(models.Model):
#     day = models.DateField(null=True, blank=True)
#     xui = models.DateField(null=True, blank=True)
