from django.db import models


class Student(models.Model):
	name = models.CharField(max_length=50, default='')
	midname = models.CharField(max_length=50, default='')
	surname = models.CharField(max_length=50,default='')
	address = models.TextField(max_length=100)
	phone = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.name

class News(models.Model):
	headline = models.CharField(max_length=40, default='')
	author = models.CharField(max_length=40, default='')
	pub_date = models.DateTimeField('date published')
	body = models.TextField()

	def __str__(self):
		return self.headline

