
from django.db.models import Model, BooleanField, NullBooleanField, CommaSeparatedIntegerField, EmailField, IPAddressField, GenericIPAddressField, URLField, FileField, ImageField, CharField, TextField, DateField, DateTimeField, TimeField, BigIntegerField, DecimalField, FloatField, IntegerField, PositiveIntegerField, PositiveSmallIntegerField, SmallIntegerField, ForeignKey, ManyToManyField, OneToOneField

import json

class JSONable:
    def as_json_dict(self):
        dictionary = {}
        for key in self.json_attributes:
            if key[-4:] == '_set':
                dictionary[key[:-4] + 's'] = list(map(
                    (lambda thing: thing.as_json_dict()),
                    getattr(self, key).all()))
            else:
                dictionary[key] = self.__dict__[key]
        
        return dictionary
    
    def as_json(self):
        return json.dumps(self.as_json_dict)
    
    @classmethod
    def all_as_json_dicts(self):
        return self.all.map(
            lambda jsonable: jsonable.as_json_dict)
    
    @classmethod
    def all_as_json(self):
        return json.dumps(self.all_as_json_dicts)

class Post(Model, JSONable):
    uuid = CharField(max_length = 255)
    creation_date = DateTimeField(auto_now_add = True)
    published_date = DateTimeField(null = True)
    published = BooleanField(default = False)
    
    def content_post(self):
        try:
            return self.linkpost
        except AttributeError:
            return self.textpost
    
    def publish(self):
        self.published = True
        self.published_date = datetime.datetime.now()
        self.save()

class LinkPost(Post):
    title = CharField(max_length = 255)
    url = URLField()
    original_url = URLField()
    description = TextField()
    provider_name = CharField(max_length = 255)
    provider_display = TextField(null = True)
    favicon_url = URLField(null = True)
    url_title = TextField()
    url_description = TextField(null = True)
    
    json_attributes = ['id',
        'title',
        'published',
        'url',
        'original_url',
        'description',
        'provider_name',
        'provider_display',
        'favicon_url',
        'comment_set']

class TextPost(Post):
    title = CharField(max_length = 255)
    content = TextField()
    
    json_attributes = ['id',
        'title',
        'published',
        'content',
        'comment_set']

class Comment(Model, JSONable):
    parent = ForeignKey('Comment', null = True)
    post = ForeignKey(Post)
    uuid = CharField(max_length = 255)
    content = TextField()
    
    json_attributes = ['uuid', 'content', 'comment_set']
    
    def children(self):
        return list(Comment.objects.filter(parent = self))
