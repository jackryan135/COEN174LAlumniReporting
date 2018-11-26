from django.urls import path
from attendance import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/edit', views.EventUpdateView.as_view(), name='event_update'),
    path('register/', views.RegisterUser, name='register'),
    path('newevent/', views.CreateEvent, name='new_event'),
    path('attend/<int:pk>', views.attend, name='attend'),
    path('reports', views.reports, name='report'),
    path('reports/<int:pk>', views.attendanceList, name='attend_list'),
    path('approve/', views.approveEvents, name = 'approve'),
    path('approve/<int:pk>', views.eventSubmittedBy, name='event_submittedBy')
]
