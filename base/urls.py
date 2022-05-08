from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.hello),
    path('faculties/', views.faculties),
    path('faculties/<str:facul>/', views.specialities),
    path('faculties/<str:facul>/<str:special>/', views.groups),
    path('faculties/<str:facul>/<str:special>/<str:group>/', views.schedule),
    # path('faculties/<str:args>/', views.specialities),
    # path('schedule/', views.schedule),


]
