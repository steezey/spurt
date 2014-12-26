from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # put link in user's inbox
    #
)
