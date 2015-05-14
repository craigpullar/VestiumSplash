from django.contrib import admin
from models import Registrant, Photo, Tag
from SlugGenerator import *

# Register your models here.
class RegistrantAdmin(admin.ModelAdmin):
	pass

class TagInline(admin.TabularInline):
	model = Tag
	extra = 1

class PhotoAdmin(admin.ModelAdmin):
	inlines = [TagInline]
	fields = ['image_path','enabled','inPool','user_name','user_email','user_link']

	def save_model(self, request, obj, form, change):
		obj.save()
		obj.slug = slugForObjectId(obj.id)
		obj.save()

admin.site.register(Registrant, RegistrantAdmin)
admin.site.register(Photo, PhotoAdmin)