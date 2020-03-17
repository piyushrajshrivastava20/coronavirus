from django.db import models

# Create your models here.
class India(models.Model):
	confirm = models.IntegerField()
	deaths= models.IntegerField()
	Recovered = models.IntegerField()
	States = models.IntegerField()