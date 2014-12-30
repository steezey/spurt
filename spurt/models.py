
from django.db.models import Model, BooleanField, NullBooleanField, CommaSeparatedIntegerField, EmailField, IPAddressField, GenericIPAddressField, URLField, FileField, ImageField, CharField, TextField, DateField, DateTimeField, TimeField, BigIntegerField, DecimalField, FloatField, IntegerField, PositiveIntegerField, PositiveSmallIntegerField, SmallIntegerField, ForeignKey, ManyToManyField, OneToOneField

import json

class JSONable:
    def as_json_dict(self):
        return \
            {k: self.__dict__[k] for k in self.json_attributes}
    
    def as_json(self):
        return json.dumps(self.as_json_dict)
    
    @classmethod
    def all_as_json_dicts(self):
        return self.all.map(
            lambda jsonable: jsonable.as_json_dict)
    
    @classmethod
    def all_as_json(self):
        return json.dumps(self.all_as_json_dicts)

class Post(Model):
    uuid = CharField(max_length = 255)
    creation_date = DateTimeField(auto_now_add = True)
    published = BooleanField(default = False)
    
    def content_post(self):
        try:
            return self.linkpost
        except AttributeError:
            return self.textpost

class LinkPost(Post, JSONable):
    title = CharField(max_length = 255)
    url = URLField()
    original_url = URLField()
    description = TextField()
    provider_name = CharField(max_length = 255)
    provider_display = TextField(null = True)
    favicon_url = URLField(null = True)
    url_title = TextField()
    url_description = TextField(null = True)
    
    json_attributes = ['id', 'title', 'published', 'url', 'original_url', 'description', 'provider_name', 'provider_display', 'favicon_url']

class TextPost(Post, JSONable):
    title = CharField(max_length = 255)
    content = TextField()
    
    json_attributes = ['id', 'title', 'published', 'content']

class Comment(Model, JSONable):
    parent = ForeignKey('Comment')
    post = ForeignKey(Post)
    uuid = CharField(max_length = 255)
    content = TextField()
    
    json_attributes = ['uuid', 'content']
    
    def children(self):
        return list(Comment.objects.filter(parent = self))
    
    def as_json_dict(self):
        dictionary = {}
        for attribute in json_attributes:
            dictionary[attribute] = self.__dict__[attribute]
        
        dictionary['children'] = map(
            (lambda child: child.as_json_dict()),
            self.children())
        
        return dictionary
