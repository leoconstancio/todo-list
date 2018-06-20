from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
	name = models.CharField(u"Category", max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

class Task(models.Model):

	PRIORITY = (
		('High', 'High'),
		('Medium', 'Medium'),
		('Low', 'Low'),
		)

	category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, default="")
	date = models.DateField(u"Date", default=timezone.now)
	time = models.TimeField(u"Time", default=datetime.datetime.now)
	description = models.TextField(u"Description")
	priority = models.CharField(u'Priority', max_length=10, choices=PRIORITY, default="Medium")
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Task"
		verbose_name_plural = "Tasks"

	def __str__(self):
		return str(self.id)
