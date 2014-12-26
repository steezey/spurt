
from spurt.models import Item
from django.http import HttpResponse

def item_create(request):
    # POST: url, uiud
    # TODO:
    # create item with URL and UIUD
    # return response
    # send to embedly

def item_edit(request):
    # POST (maybe): title, description, id, and authorUIUD
    # TODO

def item_publish(request):
    # POST (maybe): title, description, id, and authorUIUD
    # TODO

def item_inbox(request):
    # GET: uiud
    return HttpResponse(
        json.dumps(Item.filter(authorUIUD = request.GET['uiud'])
            .map(lambda item: item.as_json_dict())))

def item_public(request):
    return HttpResponse(
        json.dumps(Item.filter(public = True)
            .map(lambda item: item.as_json_dict())))
