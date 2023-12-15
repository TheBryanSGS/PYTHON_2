from django.urls import path #definir rutas o urls
from . import views
from .views import index, login, opciones, registro, reporte# desde views trae la funcion index

urlpatterns =[
    path('',views.index,name ="index"),
    path('login/', views.login, name ='login'),
    path('opciones/',views.opciones, name = 'opciones'),
    path('registro/', views.registro, name ="registro"),
    path('reporte/', views.reporte, name ="reporte")
]