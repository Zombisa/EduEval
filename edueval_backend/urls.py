"""
URL configuration for edueval_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Módulos del proyecto
    path('api/autenticacion/', include('apps.autenticacion.urls')),
    path('api/competencias-programa/', include('apps.competencias_programa.urls')),
    path('api/competencias-asignatura/', include('apps.competencias_asignatura.urls')),
    path('api/rubricas/', include('apps.rubricas.urls')),
    path('api/evaluaciones/', include('apps.evaluaciones.urls')),
]

