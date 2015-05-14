
import json
from django.shortcuts import render
from models import Registrant, Photo, Meta
from django.http import HttpResponse
import random
import re



##############
# INDEX VIEW #
##############
def index(request, image_url_token = None):

	m = Meta.objects.get(pk=1)

	if image_url_token != None:
		
		photo = Photo.objects.filter(slug=image_url_token).filter(enabled = True)

		if len(photo):
			photo = photo[0]
		else:
			photo = random.choice(Photo.objects.filter(inPool = True).filter(enabled = True))
	else:
		photo = random.choice(Photo.objects.filter(inPool = True).filter(enabled = True))

	image_path = photo.image_path

	tags = photo.tag_set.all()


	return render (request, 'index.html', {'image_path': 'backgrounds/' + str(image_path).split('/')[-1], 
		'label_positions': tags, 'length' : len(tags), 'user_name' : photo.user_name,'user_email':photo.user_email, 'num_users': m.num_users, 'user_link': photo.user_link})



########################
# CHECK EMAIL FUNCTION #
########################
def check_email(request):
	num_results = Registrant.objects.filter(email__iexact = request.POST['email']).count()

	response_data = {}
	response_data['valid'] = True;

	if num_results:
		response_data['valid'] = False;
		response_data['message'] = 'This email you requested has already been taken';
	elif not re.match("[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}",request.POST['email']):
		response_data['valid'] = False;
		response_data['message'] = 'This email did not pass validation';

	return HttpResponse(json.dumps(response_data), content_type="application/json")

###########################
# CHECK USERNAME FUNCTION #
###########################
def check_username(request):
	num_results_username = Registrant.objects.filter(username__iexact = request.POST['username']).count()

	response_data = {}
	response_data['valid'] = True;

	if num_results_username:
	 	response_data['valid'] = 0;
	 	response_data['message'] = 'This username you requested has already been taken';
	 	return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif not re.match("^[a-zA-Z0-9_]*$",request.POST['username']):
		response_data['valid'] = False;
		response_data['message'] = 'This username did not pass validation';


	return HttpResponse(json.dumps(response_data), content_type="application/json")

#####################
# REGISTER FUNCTION #
#####################
def register(request):
	
	num_results_username = Registrant.objects.filter(username__iexact = request.POST['username']).count()
	num_results_email = Registrant.objects.filter(email__iexact = request.POST['email']).count()
	
	response_data = {}
	response_data['valid'] = True;

	if num_results_username:
	 	response_data['valid'] = 0;
	 	response_data['message'] = 'This username you requested has already been taken';

	elif num_results_email:
		response_data['valid'] = 0;
	 	response_data['message'] = 'Umm...no.';

	else:
		r = Registrant(email = request.POST['email'], username = request.POST['username'], ip_address = request.META.get('REMOTE_ADDR'))
		r.email.lower()
		try:
			r.save()
			m = Meta.objects.get(pk=1)
			m.num_users += 1
			m.save()
			response_data['num_users'] = m.num_users
		except: 
			response_data['valid'] = False;
			response_data['message'] = 'We cannot sign you up at this time. Please try again later.';

	return HttpResponse(json.dumps(response_data), content_type="application/json")



###########################
# CHECK USERNAME FUNCTION #
###########################
def check_username(request):
	num_results_username = Registrant.objects.filter(username__iexact = request.POST['username']).count()

	response_data = {}
	response_data['valid'] = True;

	if num_results_username:
	 	response_data['valid'] = 0;
	 	response_data['message'] = 'This username you requested has already been taken';

	return HttpResponse(json.dumps(response_data), content_type="application/json")



############
# 404 VIEW #
############
def custom404(request):
	template = '404.html'
	return render(request,template)


