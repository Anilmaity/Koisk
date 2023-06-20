
from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    P_Id = models.CharField(max_length=100, primary_key=True, unique=True)
    Date = models.DateField(auto_now_add=True)
    Time = models.DateField(auto_now=True, blank=True)
    Promt_message = models.TextField(blank=True, max_length=1600000)
    Response = models.TextField(blank=True, max_length=1600000)
    Token = models.FloatField(default=0)
    cost = models.DecimalField(decimal_places=8,max_digits=16,default=0)
    Modelused = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return (str(self.Promt_message) +" "+str(self.Date))

