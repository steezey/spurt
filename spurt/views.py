
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

from spurt.models import *
from django.http import HttpResponse

import urllib

# python 3.4:
# from urllib import request

# python 2.7:
request = urllib

def success(**dictionary):
    dictionary['status'] = 'success'
    return HttpResponse(json.dumps(dictionary))

def failure(**dictionary):
    dictionary['status'] = 'failed'
    return HttpResponse(json.dumps(dictionary))

embedly_key = '2349d9cd48b64d988389fb4af2792a45'

def embedlify(url):
    return json.loads(request.urlopen(
            'http://api.embed.ly/1/extract?key=' + 
            embedly_key + 
            '&url=' + 
            urllib.quote(url))\
        .read())

def embedlify_linkpost(linkpost, url):
    embedly = embedlify(url)
    for (attribute, name) in [
            ('url', 'url'),
            ('original_url', 'original_url'),
            ('provider_name', 'provider_name'),
            ('provider_display', 'provider_display'),
            ('favicon_url', 'favicon_url'),
            ('url_title', 'title'),
            ('url_description', 'description')]:
        linkpost.__dict__[attribute] = embedly[name]


@csrf_exempt
def linkpost_create(request):
    # POST: url, uuid
    
    linkpost = LinkPost()
    linkpost.uuid = request.POST['uuid']
    embedlify_linkpost(linkpost, request.POST['url'])
    linkpost.save()
    
    return success(id = linkpost.id)

@csrf_exempt
def linkpost_create_and_publish(request):
    # POST: url, uuid, title, description
    
    linkpost = LinkPost()
    for attribute in ['uuid', 'title', 'description']:
        linkpost.__dict__[attribute] = request.POST[attribute]
    
    embedlify_linkpost(linkpost, request.POST['url'])
    linkpost.publish()
    linkpost.save()
    
    return success(id = linkpost.id)

@csrf_exempt
def linkpost_edit(request):
    # POST: title, description, id, and uuid
    
    linkpost = get_object_or_404(
        LinkPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    linkpost.title = request.POST['title']
    linkpost.description = request.POST['description']
    linkpost.save()
    return success()

@csrf_exempt
def linkpost_publish(request):
    # POST: uuid, id
    
    linkpost = get_object_or_404(
        LinkPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    linkpost.publish()
    linkpost.save()
    return success()

@csrf_exempt
def textpost_create(request):
    # POST: title, description, uuid
    
    textpost = TextPost()
    for attribute in ['title', 'description', 'uuid']:
        textpost.__dict__[attribute] = request.POST[attribute]
    
    textpost.save()
    
    return success(id = textpost.id)

@csrf_exempt
def textpost_create_and_publish(request):
    # POST: title, description, uuid
    
    textpost = TextPost()
    for attribute in ['title', 'description', 'uuid']:
        textpost.__dict__[attribute] = request.POST[attribute]
    
    textpost.publish()
    textpost.save()
    
    return success(id = textpost.id)

@csrf_exempt
def textpost_edit(request):
    # POST: title, description, id, and uuid
    
    textpost = get_object_or_404(
        TextPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    textpost.title = request.POST['title']
    textpost.description = request.POST['description']
    textpost.save()
    return success(id = textpost.id)

@csrf_exempt
def textpost_publish(request):
    # POST: uuid, id
    
    textpost = get_object_or_404(
        TextPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    textpost.publish()
    textpost.save()
    return success(id = textpost.id)

@csrf_exempt
def post_public(request):
    # GET: (none)
    
    return HttpResponse(
        json.dumps(list(map(
            (lambda post: post.content_post().as_json_dict()),
            Post.objects\
                .order_by('-published_date')\
                .filter(published = True)))))

@csrf_exempt
def post_inbox(request):
    # GET: uuid
    
    return HttpResponse(
        json.dumps(list(map(
            (lambda post: post.content_post().as_json_dict()),
            Post.objects.order_by('-published_date').filter(
                published = False,
                uuid = request.GET['uuid'])))))

@csrf_exempt
def comment_create(request):
    # POST: post_id, uuid, content, (optional) parent_id
    
    comment = Comment(
        post = get_object_or_404(Post, id = request.POST['post_id']),
        uuid = request.POST['uuid'],
        content = request.POST['content'])
    if request.POST.has_key('parent_id'):
        comment.parent = get_object_or_404(
            Comment,
            id = request.POST['parent_id'])
    
    comment.save()
    
    return success(id = comment.id)
