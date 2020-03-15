from django.contrib import admin

# Register your models here.
from .models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id','name','destination','car','pickup','nid')
    list_editable = ('pickup',)
    list_per_page = 10
    search_fields = ('name','nid','car','pickup')
    list_filter = ('car','pickup','date_added')

admin.site.register(Driver,DriverAdmin)