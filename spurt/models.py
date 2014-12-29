
from django.db.models import Model, BooleanField, NullBooleanField, CommaSeparatedIntegerField, EmailField, IPAddressField, GenericIPAddressField, URLField, FileField, ImageField, CharField, TextField, DateField, DateTimeField, TimeField, BigIntegerField, DecimalField, FloatField, IntegerField, PositiveIntegerField, PositiveSmallIntegerField, SmallIntegerField, ForeignKey, ManyToManyField, OneToOneField

import json

print('ELEPHANT MODELS')

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

class Item(Model, JSONable):
    title = CharField(max_length = 255)
    authorUIUD = CharField(max_length = 255)
    creation_date = DateTimeField(auto_now_add = True)
    published = BooleanField(default = False)
    url = URLField()
    original_url = URLField()
    content = TextField()
    description = TextField()
    provider_name = CharField(max_length = 255)
    provider_display = TextField()
    favicon_url = URLField()
    
    json_attributes = ['id', 'title', 'published', 'url', 'original_url', 'content', 'description', 'provider_name', 'provider_display', 'favicon_url']
