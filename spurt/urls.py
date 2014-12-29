from django.conf.urls import patterns, include, url
from django.contrib import admin

from spurt import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/create', views.item_create),
    url(r'^items/edit', views.item_edit),
    url(r'^items/publish', views.item_publish),
    url(r'^items/inbox', views.item_inbox),
    url(r'^items/public', views.item_public),
)

print('ELEPHANT URLS')