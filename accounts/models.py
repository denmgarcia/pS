from django.db import models

class AddressBook(models.Model):
	first_name = models.CharField(max_length=50, default='')
	last_name = models.CharField(max_length=50,default='')
	phone = models.CharField(max_length=11, default='')
	address = models.TextField(max_length=100)

	def __str__(self):
		return '{} {}'.format(self.first_name,self.last_name)

class News(models.Model):
	headline = models.CharField(max_length=40, default='')
	author = models.CharField(max_length=50, default='')
	pub_date = models.DateTimeField('date published')
	body = models.TextField()

	def __str__(self):
		return self.headline

