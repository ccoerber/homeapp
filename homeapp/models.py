from django.db import models

# Create your models here.
class Location(models.Model):
	name_text = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name_text
				
class Device(models.Model):
	type_choices = (
		("Controller", "Controller"),
		("Sensor", "Sensor"),
		("Other", "Other")
	)
	name_text = models.CharField(max_length=100, blank=False)
	location_fk = models.ForeignKey(Location, on_delete=models.CASCADE)
	type_list = models.CharField(max_length=50,choices=type_choices)
	
	def __str__(self):
		return self.name_text

	def is_type(self):
		return self.type_text
