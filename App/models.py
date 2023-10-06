from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class job(models.Model):
    "This is Job Table"
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50,null=True)
    salary = models.FloatField()
    mail = models.EmailField(default='@gmail.com')
    creater = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.position
