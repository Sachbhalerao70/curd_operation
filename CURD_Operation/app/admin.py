from django.contrib import admin
from .models import appModel


# Register your models here.
class appAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','esal','ecity','econtact','edepart']

admin.site.register(appModel,appAdmin)

