from django.conf.urls import patterns, include, url
from django.contrib import admin

from spurt import views

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    
    # Create link post and publish. POST: url, uuid, title, description
    url(r'^link-posts/create-and-publish', views.linkpost_create_and_publish),
    
    # Create link post. POST: url, uuid
    url(r'^link-posts/create', views.linkpost_create),
    
    # Edit link post. POST: title, description, id, and uuid
    url(r'^link-posts/edit', views.linkpost_edit),
    
    # Publish link post. POST: uuid, id, (optional) title, (optional)
    # description
    url(r'^link-posts/publish', views.linkpost_publish),
    
    # [Internal use] Receive scrape. GET: scrape_token
    url(r'^link-posts/receive-scrape', views.linkpost_receive_scrape),
    
    # Create text post and publish. POST: title, content, uuid
    url(r'^text-posts/create-and-publish', views.textpost_create_and_publish),
    
    # Create text post. POST: title, content, uuid
    url(r'^text-posts/create', views.textpost_create),
    
    # Edit text post. POST: title, content, id, and uuid
    url(r'^text-posts/edit', views.textpost_edit),
    
    # Publish text post. POST: uuid, id, (optional) title, (optional) content
    url(r'^text-posts/publish', views.textpost_publish),
    
    # Get published posts. GET: (none)
    url(r'^posts/public', views.post_public),
    
    # Get posts in inbox. GET: uuid
    url(r'^posts/inbox', views.post_inbox),
    
    # Create new comment. POST: (optional) parent_id, post_id, uuid, content
    url(r'^comments/create', views.comment_create),
    
    # Get uuid associated with auth code. GET: auth_code
    url(r'^auth-code-to-uuid', views.auth_code_to_uuid),
    
    # Get current auth code. GET: uuid
    url(r'^auth-code', views.auth_code),
)

"""

API Note:

A link post has the following attributes: id, title, url, original_url, description, scraped_title, domain, rddme_url, author_name, author, dek, lead, lead_image, scraped_pub_date, embedly_safe, favicon, content, kind

"""
