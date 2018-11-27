# Authors: Sam Burns, Simran Judge, Jack Ryan
# admin.py: Specifies the fields visible on the event creation form on the Django administration page
from django.contrib import admin
from attendance.models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date',
                    'time', 'numAttend', 'approved')
    list_filter = ('approved', 'date')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'location', ('date', 'time')),
        }),
        ('Approval', {
            'fields': ('approved',),
        }),
    )


admin.site.register(Event, EventAdmin)
