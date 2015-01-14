
import datetime
import json
import re
import urlparse
import urllib2

from django.db.models import Model, BooleanField, NullBooleanField, CommaSeparatedIntegerField, EmailField, IPAddressField, GenericIPAddressField, URLField, FileField, ImageField, CharField, TextField, DateField, DateTimeField, TimeField, BigIntegerField, DecimalField, FloatField, IntegerField, PositiveIntegerField, PositiveSmallIntegerField, SmallIntegerField, ForeignKey, ManyToManyField, OneToOneField

class InvalidURL(Exception): pass

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

class EmbedlyResponse(Model):
    url = TextField()
    response = TextField()

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
    url = TextField()
    original_url = TextField()
    description = TextField(null = True)
    scraped_title = TextField(null = True)
    domain = TextField(null = True)
    rddme_url = TextField(null = True)
    author_name = TextField(null = True)
    authors = TextField(null = True)
    dek = TextField(null = True)
    lead = TextField(null = True)
    lead_image = TextField(null = True)
    pub_date = DateTimeField(null = True)
    embedly_safe = TextField(null = True)
    favicon = TextField(null = True)
    content = TextField(null = True)
    kind = CharField(max_length = 255, default = 'link')
    
    def as_json_dict(self):
        dictionary = Post.as_json_dict(self)
        
        return dictionary
    
    json_attributes = [
        'id',
        'title',
        'url',
        'original_url',
        'description',
        'scraped_title',
        'domain',
        'rddme_url',
        'author_name',
        'author',
        'dek',
        'lead',
        'lead_image',
        'pub_date',
        'embedly_safe',
        'favicon',
        'content',
        'kind']
    
    def scrape(self, url):
        url = urlparse.urlparse(url)
        
        if url.netloc is '':
            raise InvalidURL("URL netloc is ''")
        
        url = urlparse.ParseResult(
            scheme = url.scheme or 'http',
            netloc = url.netloc,
            path = url.path,
            params = url.params,
            query = url.query,
            fragment = url.fragment)
        
        gauss_url = \
            'http://gauss.elasticbeanstalk.com/' + \
            '?key=4a9fdf362ffff48fc64f2c3621166a75' + \
            '&url=' + url.geturl()
        
        scraped = json.loads(urllib2.urlopen(gauss_url).read())
        
        for attribute in scraped.keys():
            self.__dict__[attribute] = scraped[attribute]
        
        self.save()

class TextPost(Post):
    title = CharField(max_length = 255)
    content = TextField()
    kind = CharField(max_length = 255, default = 'text')
    
    json_attributes = [
        'id',
        'title',
        'published',
        'content',
        'comment_set',
        'kind']

class Comment(Model, JSONable):
    parent = ForeignKey('Comment', null = True)
    post = ForeignKey(Post)
    uuid = CharField(max_length = 255)
    content = TextField()
    
    json_attributes = [
        'id',
        'uuid',
        'content',
        'comment_set']
    
    def children(self):
        return list(Comment.objects.filter(parent = self))
