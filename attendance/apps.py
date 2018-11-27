# Authors: Sam Burns, Simran Judge, Jack Ryan
# apps.py: Registers the different apps within the Django system
from django.apps import AppConfig


# Class Name: AttendanceConfig
# Parameters: AppConfig
# Description: This registers the attendance app with the global Django system
class AttendanceConfig(AppConfig):
    name = 'attendance'
