
import json

from spurt.models import Item
from django.http import HttpResponse

import urllib

def embedlify(url):
    request_url = \
        'http://api.embed.ly/1/extract?key=' + \
        embedly_key + \
        '&url=' + \
        urllib.quote(url)

def item_create(request):
    pass
    # POST: url, uiud
    # TODO:
    # create item with URL and UIUD
    # return response
    # send to embedly

def item_edit(request):
    pass
    # POST (maybe): title, description, id, and authorUIUD
    # TODO

def item_publish(request):
    pass
    # POST (maybe): title, description, id, and authorUIUD
    # TODO

def item_inbox(request):
    # GET: uiud
    return HttpResponse(
        json.dumps(list(map(
            (lambda item: item.as_json_dict()),
            Item.objects.filter(
                authorUIUD = request.GET['uiud'])))))

def item_public(request):
    return HttpResponse(
        json.dumps(list(map(
            (lambda item: item.as_json_dict()),
            Item.objects.filter(published = True)))))
