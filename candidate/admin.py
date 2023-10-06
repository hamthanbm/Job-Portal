from django.contrib import admin
from .models import *

class control(admin.ModelAdmin):
    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return CandidateJobMap.objects.all()
        else:
            return CandidateJobMap.objects.filter(job_owner=request.user)

# Register your models here.
admin.site.register(CandidateJobMap,control)