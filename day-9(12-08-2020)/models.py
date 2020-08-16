from django.db import models

# Create your models here.
class Emp(models.Model):
	fname=models.CharField(max_length=30,null=True)
	lname=models.CharField(max_length=30)
	age=models.IntegerField(null=True)

	def __str__(self):
		return self.fname+" "+self.lname+" "+str(self.age)

