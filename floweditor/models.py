from django.db import models

# Create your models here.

class B1if(models.Model):
	name		= models.CharField(max_length=100,null=True)
	server		= models.CharField(max_length=100)
	path		= models.CharField(max_length=300,default='/B1iXcellerator/exec/webdav/com.sap.b1i.vplatform.scenarios.design/')
	port		= models.CharField(max_length=8,default='8080')
	user		= models.CharField(max_length=24)
	password	= models.CharField(max_length=24)
	def __unicode__(self):
		return self.name+" ("+self.server+")"

class B1file(models.Model):
	contents	= models.TextField()
	dirty		= models.BooleanField(default=False)
	flow	= models.CharField(max_length=200)
	filename	= models.CharField(max_length=200)
	path		= models.CharField(max_length=300)
	def __unicode__(self):
		return self.flow+"/"+self.filename

