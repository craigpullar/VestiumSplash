from django.conf.urls import url

from landing_page import views

urlpatterns = [
    url(r'^check_email_address',views.check_email),
    url(r'^register',views.register),
    url(r'^check_username',views.check_username)
]
