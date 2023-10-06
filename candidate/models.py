from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CandidateJobMap(models.Model):
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    Job = models.ForeignKey('App.job',on_delete=models.CASCADE)
    job_owner = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.candidate.username}  -  {self.Job.position}"