from django.urls import path
from . import views
urlpatterns = [
    path('control_panel/', views.control_panel, name='control_panel'),
    path('shortjob/', views.shortjob, name='shortjob'),
    path('cronjob/', views.cronjob, name='cronjob'),
    path('perday/', views.perday, name='perday'),
    path('perdate/', views.perdate, name='perdate'),
    path('pertime/', views.pertime, name='pertime'),
]