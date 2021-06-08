from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class anntbl(models.Model):
	anid = models.AutoField(primary_key=True)
	upload = models.ImageField(blank=True, null = True, upload_to ='uploads/') 

	def __str__(self):
		return str(self.upload)

class Roles(models.Model):
	role_id = models.AutoField(primary_key=True)
	role = models.CharField(max_length=255, blank=True, null = True)

	def __str__(self):
		return self.role

class Author(models.Model):        
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


    # additional fields
    middle_initial = models.CharField(max_length=255, blank=True, null = True)
    official_designation = models.CharField(max_length=255, blank=True, null = True)
    office_or_agency = models.CharField(max_length=255, blank=True, null = True)
    sector = models.CharField(max_length=255, blank=True, null = True)
    mobile = models.CharField(max_length=255, blank=True, null = True)
    role = models.ForeignKey(Roles, default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(blank=True, null = True, upload_to ='uploads/')

    def __str__(self):
        return self.user.username


# Create your models here.
