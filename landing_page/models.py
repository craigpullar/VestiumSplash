from django.db import models
from validators import *

class Registrant(models.Model):
	email = models.CharField(max_length= 255, unique=True,validators=[email_regex])

	username = models.CharField(max_length = 63, unique=True, validators=[username_regex])

	date_time = models.DateTimeField(auto_now_add=True, blank=True)

	ip_address = models.IPAddressField(blank = True,validators=[ip_regex])

	def  __unicode__(self):
		return "%s (%s)" % (self.username, self.email)
		
def background_upload_to():
	return '/Users/craigpullar/Vestium_Landing_Page/vestium/static/backgrounds/'

class Photo(models.Model):
	slug = models.CharField(max_length= 255)
	image_path = models.FileField(upload_to=background_upload_to())
	enabled = models.BooleanField(default=True)
	inPool = models.BooleanField(default=False)
	user_name = models.CharField(max_length = 100)
	user_email = models.CharField(max_length= 255,unique=False)
	user_link = models.CharField(max_length=255)

	def __unicode__(self):
		return "{0}".format(self.slug)

class Tag(models.Model):
	photo = models.ForeignKey(Photo)
	x = models.IntegerField()
	y = models.IntegerField()
	angle = models.IntegerField()
	colour = models.CharField(max_length = 10, default = 'black', blank=True)


class Meta(models.Model):
	num_users = models.IntegerField()




