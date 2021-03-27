"""icjcf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core.views import Register

urlpatterns = [
    path('adminicjcf/', admin.site.urls),
    path('accounts/register', Register.as_view(), name="register"),
    path('accounts/', include('allauth.urls')),
    path("resourcecenter/", include("resourcecenter.urls")),
    path("", include("core.urls")),
]

handler404 = "core.views.handler404"
handler500 = "core.views.handler500"
handler400 = "core.views.handler400"
handler403 = "core.views.handler403"
