from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App.models import job
from candidate.models import CandidateJobMap
from tkinter import *
# Create your views here. 

def home(request):
    data = job.objects.all()
    if request.method == 'POST':
        Selected = request.POST.getlist('okay')
        person = request.user
        # jo = job.objects.all().values()
        # for i in jo:
        #     print(i)
        while (CandidateJobMap.objects.filter(candidate_id=person.id)):
            wont = CandidateJobMap.objects.filter(candidate_id=person.id)
            wont.delete()
        for i in Selected:
            job_Record = job.objects.get(position=i)
            owner = User.objects.get(id=job_Record.creater_id)
            s = CandidateJobMap(candidate_id=person.id,
                                Job_id=job_Record.id, job_owner=owner.username)
            s.save()
    return render(request, "home.html", {'j': data})

@ login_required
def write(request):
    if request.user.last_name == '( Admin )' or request.user.last_name == '( client )':
        if request.user.last_name == '( Admin )':
            j = job.objects.all()
            jm = CandidateJobMap.objects.all()
        else:
            j = job.objects.filter(creater=request.user)
            jm = CandidateJobMap.objects.filter(job_owner=request.user)
        return render(request, 'blank.html',{"my_job":j,"applay_job":jm})
    else:
        return render(request, 'free.html')

def register(request):
    if request.method == 'POST':
        try:
            name=request.POST["username"]
            email=request.POST["email"] 
            password1=request.POST["password1"]
            password2=request.POST["password2"]

            if password1 == password2:
                user=User.objects.create_user(
                    username=name, email=email, password=password1)
                user.is_staff=True
                # user.is_superuser=True
                user.save()
                messages.success(
                    request, 'Your account has been created! You are able to login')
                return redirect('Log')
            else:
                messages.warning(request, 'Password Mismatching...!!!')
                return redirect('Register')
        except Exception as d:
            messages.error(
                request, f'User Register Failed.. - {d} -')
            return redirect('Register')

    else:
        form=CreateUserForm()
        return render(request, "register.html", {'form': form})


@ login_required
def profile(request):
    return render(request, "profile.html")
