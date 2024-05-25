from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recordatorios, name='lista_recordatorios'),
    path('/crear/', views.crear_recordatorio, name='crear_recordatorio'),
    path('/actualizaciones/', views.obtener_actualizaciones, name='obtener_actualizaciones'),
]
