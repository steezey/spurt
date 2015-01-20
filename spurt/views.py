
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from spurt.models import *

def success(**dictionary):
    dictionary['status'] = 'success'
    return HttpResponse(json.dumps(dictionary))

def failure(**dictionary):
    dictionary['status'] = 'failed'
    return HttpResponse(json.dumps(dictionary))

@csrf_exempt
def linkpost_create(request):
    # POST: url, uuid
    
    try:
        linkpost = LinkPost()
        linkpost.uuid = request.POST['uuid']
        linkpost.scrape(request.POST['url'])
        linkpost.save()
        
        return success(id = linkpost.id)
    except InvalidURL:
        return failure(message = 'Invalid URL', url = request.POST['url'])

@csrf_exempt
def linkpost_create_and_publish(request):
    # POST: url, uuid, title, description
    
    linkpost = LinkPost()
    for attribute in ['uuid', 'title', 'description']:
        linkpost.__dict__[attribute] = request.POST[attribute]
    
    try:
        linkpost.scrape(request.POST['url'])
        linkpost.publish()
        linkpost.save()
        
        return success(id = linkpost.id)
    except InvalidURL:
        return failure(message = 'Invalid URL', url = request.POST['url'])

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
    # POST: uuid, id, (optional) title, (optional) description
    
    linkpost = get_object_or_404(
        LinkPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    for attribute in ['title', 'description']:
        linkpost.__dict__[attribute] = \
            request.POST.get(attribute, linkpost.__dict__[attribute])
    linkpost.publish()
    linkpost.save()
    return success()

@csrf_exempt
def textpost_create(request):
    # POST: title, description, uuid
    
    textpost = TextPost()
    for attribute in ['title', 'content', 'uuid']:
        textpost.__dict__[attribute] = request.POST[attribute]
    
    textpost.save()
    
    return success(id = textpost.id)

@csrf_exempt
def textpost_create_and_publish(request):
    # POST: title, description, uuid
    
    textpost = TextPost()
    for attribute in ['title', 'content', 'uuid']:
        textpost.__dict__[attribute] = request.POST[attribute]
    
    textpost.publish()
    textpost.save()
    
    return success(id = textpost.id)

@csrf_exempt
def textpost_edit(request):
    # POST: title, content, id, and uuid
    
    textpost = get_object_or_404(
        TextPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    textpost.title = request.POST['title']
    textpost.content = request.POST['content']
    textpost.save()
    return success(id = textpost.id)

@csrf_exempt
def textpost_publish(request):
    # POST: uuid, id, (optional) title, (optional) content
    
    textpost = get_object_or_404(
        TextPost,
        id = request.POST['id'],
        uuid = request.POST['uuid'])
    textpost.title = request.POST.get('title', textpost.title)
    textpost.content = request.POST.get('content', textpost.content)
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
            Post.objects.order_by('-creation_date').filter(
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

@csrf_exempt
def auth_code(request):
    try:
        user = User.objects.get(uuid = request.GET['uuid'])
    except ObjectDoesNotExist:
        user = User()
        user.uuid = request.GET['uuid']
        user.save()
    
    return success(auth_code = user.get_or_create_auth_code())

def auth_code_to_uuid(request):
    user = get_object_or_404(User, auth_code = request.GET['auth_code'])
    if user.auth_code_expiry < timezone.now():
        return failure(message = 'Auth code expired.')
    else:
        return success(uuid = user.uuid)
