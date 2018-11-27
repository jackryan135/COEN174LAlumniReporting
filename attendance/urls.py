#simran
from django.urls import path
from attendance import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    # path('register/', views.RegisterUser, name='register'),
    path('events/<int:pk>/edit', views.EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete', views.deleteEvent, name='delete_event'),
    path('newevent/', views.CreateEvent, name='new_event'),
    path('attend/<int:pk>', views.attend, name='attend'),
    path('reports', views.reports, name='report'),
    path('reports/<int:pk>', views.attendanceList, name='attend_list'),
    path('reports/delete_alumni/<int:pk>', views.deleteAlumni, name='delete_alumni'),
    path('approve/', views.approveEvents, name = 'approve'),
    path('approve/<int:pk>/submitted_by', views.eventSubmittedBy, name='event_submittedBy'),
    path('approve/<int:pk>/approved', views.eventApproved, name='event_approved'),
    path('approve/<int:pk>/denied', views.eventDenied, name='event_denied'),
]
