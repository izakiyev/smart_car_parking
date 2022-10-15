from django.contrib import admin

# Register your models here.
from .models import Room,Customer

admin.site.register(Room)
admin.site.register(Customer)

