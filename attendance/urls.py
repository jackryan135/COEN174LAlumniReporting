from django.urls import path
from attendance import views


urlpatterns = [
    path('', views.index, name='index')
]
