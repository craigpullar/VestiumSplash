from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from django.contrib import admin
from landing_page import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/',include('landing_page.urls')),
    url(r'^i/(?P<image_url_token>[a-zA-Z0-9]{8})',views.index, name='index'),
    url(r'^$',views.index, name='index'),
)

handler404 = 'landing_page.views.custom404'

# 

