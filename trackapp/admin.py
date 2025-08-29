from django.contrib import admin
from .models import Package , Subscriber, Contact




admin.site.register(Package)
admin.site.register(Subscriber)
admin.site.register(Contact)

#@admin.register(Package)
#class PackageAdmin(admin.ModelAdmin):
    #list_display = ('tracking_id','sender_name','reciever_name', 'reciever_email','status', 'created_at', 'updated_at')
