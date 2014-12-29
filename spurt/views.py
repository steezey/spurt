
from django.views.decorators.csrf import csrf_exempt
import json

from spurt.models import Item
from django.http import HttpResponse

import urllib

# python 3.4:
# from urllib import request

# python 2.7:
request = urllib

def success(**dictionary):
    dictionary['status'] = 'success'
    return HttpResponse(json.dumps(dictionary))

def failed(**dictionary):
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

@csrf_exempt
def item_create(request):
    # POST: url, uuid
    
    item = Item()
    item.authorUUID = request.POST['uuid']
    
    embedly = embedlify(request.POST['url'])
    for attribute in [
            'url', 
            'original_url', 
            'provider_name', 
            'provider_display', 
            'favicon_url']:
        item.__dict__[attribute] = embedly[attribute]
    
    item.save()
    
    return success(id = item.id)

@csrf_exempt
def item_edit(request):
    # POST: title, description, id, and authorUUID
    
    items = list(Item.objects.filter(
        id = request.POST['id'],
        authorUUID = request.POST['uuid']))
    
    if len(items) == 0:
        return failure(message = 
            'Cannot find item with id "' + request.POST['id'] + \
            ' and uuid ' + request.POST['uuid'])
    else:
        item = items[0]
        item.title = request.POST['title']
        item.description = request.POST['description']
        item.save()
        return success()

@csrf_exempt
def item_publish(request):
    try:
        item = Item.objects.get(
            id = request.POST['id'],
            authorUUID = request.POST['uuid'])
        item.title = request.POST['title']
        item.description = request.POST['description']
        item.published = True
        item.save()
        return success()
    except DoesNotExist:
        return failure(message = 
            'Cannot find item with id "' + request.POST['id'] + \
            ' and uuid ' + request.POST['uuid'])

def item_inbox(request):
    # GET: uuid
    
    return HttpResponse(
        json.dumps(list(map(
            (lambda item: item.as_json_dict()),
            Item.objects.filter(
                authorUUID = request.GET['uuid'])))))

def item_public(request):
    return HttpResponse(
        json.dumps(list(map(
            (lambda item: item.as_json_dict()),
            Item.objects.filter(published = True)))))
