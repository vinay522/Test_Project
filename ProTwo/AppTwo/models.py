from django.db import models

# Create your models here.

class Users_db(models.Model):
	name = models.CharField(max_length=100)
	phno = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)

	def __str__(self):
		return self.name
