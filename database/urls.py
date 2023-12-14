from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), #desde el carpeta task trae el archivo urls
    path('app/', include('app.urls'))
]