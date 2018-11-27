# Authors: Sam Burns, Simran Judge, Jack Ryan
# urls.py: Specify the global URL patterns which Django uses to match URL requests to specific views.
"""AlumniReporting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from attendance.forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
    path('', RedirectView.as_view(url='/attendance/')),
    path('accounts/', include('django.contrib.auth.urls'),
         {'authentication_form': LoginForm}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
