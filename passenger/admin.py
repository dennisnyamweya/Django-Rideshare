from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Passenger

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','email','pickup','nid')
    list_editable = ('pickup',)
    list_per_page = 10
    search_fields = ('name','nid','gender','pickup','email')
    list_filter = ('gender','pickup','date_added')


admin.site.register(Passenger,PassengerAdmin)
admin.site.unregister(Group)