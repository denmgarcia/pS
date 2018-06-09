from django.db import models


class Student(models.Model):
	name = models.CharField(max_length=50, default='')
	midname = models.CharField(max_length=50, default='')
	surname = models.CharField(max_length=50,default='')
	address = models.CharField(max_length=100, default='')
	phone = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.name