from django.conf.urls.defaults import *
from django.contrib import admin
from faq.views import faq_list_by_group, submit_faq
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url (r'^$', faq_list_by_group, name = 'faq_list_by_group'),
    url (r'^submit/$', submit_faq, name = 'faq_submit'),
    url (r'^submit-success/$', direct_to_template, {'template': 'faq/submit_success.html'}, name = 'faq_submit_success'),
)
