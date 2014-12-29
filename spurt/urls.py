from django.conf.urls import patterns, include, url
from django.contrib import admin

from spurt import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Create new item. POST: url, uiud
    url(r'^items/create', views.item_create),
    # Edit item. POST: title, description, id, and authorUIUD
    url(r'^items/edit', views.item_edit),
    # Publish item. GET: uiud
    url(r'^items/publish', views.item_publish),
    # Get items in inbox. GET: uiud
    url(r'^items/inbox', views.item_inbox),
    # Get public items.
    url(r'^items/public', views.item_public),
)