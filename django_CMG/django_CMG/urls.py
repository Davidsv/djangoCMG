from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoCMG.views.home', name='home'),
    # url(r'^djangoCMG/', include('djangoCMG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^thedate/', 'screen.views.current_datetime'),

    url(r'^kanal/(?P<infochannel_id>\d)', 'screen.views.info'),

    url(r'^checkmessageexists/$', 'screen.views.checkmessageexists')
)
