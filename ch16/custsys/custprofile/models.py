from django.db import models

class CustDB(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=30)
	age = models.CharField(max_length=3)
	sex = models.CharField(max_length=1)
	tel = models.CharField(max_length=10)
	address = models.CharField(max_length=200)
	class Meta:
		db_table = "CustDB"