from django.db import models
from django.utils import timezone
from django.urls import reverse


class Item(models.Model):
	text = models.TextField(default='')
	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse('task_detail', kwargs={'id': str(self,id)})

	@property
	def tags(self):
		return ', '.join(tag.tag_name for tag in self.tag_set.all())

	#is_active = models.BooleanField(default=True)

	#title = models.CharField(max_length=100, default='', blank=True)
	
	#modified_on = models.DateField(auto_now=True)
	#created_on = models.DateField(auto_now_add=True)
	
	#modified_on = models.DateTimeField(auto_now=True)
	#created_on = models.DateTimeField(auto_now_add=True)
	
	#hours_done = models.DecimalField(max_digits=4, decimal_places=2)

class Tag(models.Model):
	tag_name = models.CharField(max_length=100)
	tagged_item = models.ForeignKey('Item', on_delete=models.CASCADE)