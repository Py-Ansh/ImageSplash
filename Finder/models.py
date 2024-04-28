from django.db import models

# Create your models here.


class Contact(models.Model):
	
	email = models.EmailField(max_length=100)
	suggestions = models.TextField()
	date = models.DateField(default=None)

	def __str__(self):
		return self.email