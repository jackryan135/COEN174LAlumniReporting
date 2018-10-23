from django.urls import path
from attendance import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('register/', views.RegisterUser, name='register'),
    path('newevent/', views.CreateEvent, name='new_event'),
    path('attend/<int:pk>', views.attend, name='attend'),
    path('reports', views.ReportListView.as_view(), name='report'),
]
