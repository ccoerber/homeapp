from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:loc_id>/', views.location, name='location'),
    path('<int:sensor_id>/sensor', views.sensor, name='sensor')
    ]
