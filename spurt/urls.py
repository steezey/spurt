from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/create', spurt.views.create),
    url(r'^items/edit', spurt.views.edit),
    url(r'^items/publish', spurt.views.publish),
    url(r'^items/inbox', spurt.views.inbox),
    url(r'^items/public', spurt.views.public),
)
