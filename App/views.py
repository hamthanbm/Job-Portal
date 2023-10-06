from django.shortcuts import render
from .models import job

# Create your views here.
def home(i):
    data = job.objects.all()
    return render(i,'sajith.html',{'j':data})
