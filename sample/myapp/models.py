from django.db import models
from django.contrib import admin
class players(models.Model):
    player_name=models.CharField(max_length=20)
    team_name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    weight=models.IntegerField()

class playersAdmin(admin.ModelAdmin) :
    list_display=('player_name','team_name','salary','age','weight')   



# Create your models here.
