"""
URLs for routing paralleltext application
"""

from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paralleltext.views.home', name='home'),
    # url(r'^paralleltext/', include('paralleltext.foo.urls')),
    url(r'^$', 'home.views.index'),
    url(r'^login/', 'users.views.user_auth'),
    url(r'^logout/', 'users.views.user_logout'),
    url(r'^register/', 'users.views.user_reg'),
    url(r'^account/', 'users.views.user_acct'),
    url(r'^account_pass/', 'users.views.user_acct_pass'),
    url(r'^account_delete/', 'users.views.del_acct'),
    #url(r'^ptext/', 'ptext.views.popup_demo'),
    url(r'^parallel_display/', 'parallel_display.views.pdisplay'),
    url(r'^upload/', 'content_mgmt.views.upload'),
    url(r'^search/', ''),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
