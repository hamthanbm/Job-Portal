from django.contrib import admin
from .models import *


class JA(admin.ModelAdmin):
    exclude = ('creater',)
    list_display = ('position', 'creater',)

    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return job.objects.all()
        else:
            return job.objects.filter(creater=request.user)
    
    def get_list_display(self, request, *ar, **k):
        if request.user.is_superuser:
            return ('position', 'creater',)
        else:
            return ('position',)

    def save_model(self, request, obj, form, change):
        obj.creater = request.user
        obj.save()


# Register your models here.
admin.site.register(job, JA)
