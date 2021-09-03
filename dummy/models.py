from django.db import models

class CronMon(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)
	status = models.BooleanField(default=False)
	def __str__(self):
		return f"{self.name.upper()}"