from django.db import models

class Cust(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=30)