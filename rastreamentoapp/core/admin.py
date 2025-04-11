from django.contrib import admin
from .models import User, Vehicle, Location, Geofence, Alert, Report, Command

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Geofence)
admin.site.register(Alert)
admin.site.register(Report)
admin.site.register(Command)