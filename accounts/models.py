from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	name		= models.CharField(max_length=100)
	disabled	= models.BooleanField(default=False)
	company		= models.CharField(max_length=100,null=True)
	def __unicode__(self):
		return self.name

class BiffyUser(models.Model):
	user 		= models.OneToOneField(User,null=True, related_name='biffyuser')
	account		= models.ForeignKey(Account,null=True)
	def __unicode__(self):
		return "Biffy: "+self.user.username

