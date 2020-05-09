import os.path
from datetime import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.

class Title(models.Model):
    title = models.CharField(max_length=300)
    materials = models.CharField(max_length=800,blank=True)
    resource = models.URLField(max_length=150,blank=True)
    update = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField('date published')
   
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
   
    def url(self):
        #if self.image:
            #return self.image
        #else:
        return os.path.join('/',settings.MEDIA_URL, "images", os.path.basename(str(self.image)))

    def image_tag(self):
        return mark_safe('<img src="{}" width="80" height="80" />'.format(self.url()) )
        #return mark_safe('<img src="{http://127.0.0.1:8000/media/images/tapping.jpg}" width="100 height="100" />')
    image_tag.short_description = 'Thumbnail'

    def resource_link(self):
        return mark_safe('<a href="{}">Resource</a>'.format(self.resource) )
        #return ('<a href="%s">Resource</a>' % self.resource)
    resource_link.allow_tags = True

    #def __unicode__(self):
        #return self.title
        #return self.show_url
     
    
    #def get_absolute_url(self):
        #return "/%i/" % self.id

    #return mark_safe('<a href="%s">Resource<a/>' % url_link)
        #return u'<a href="%s">Resource</a>' % (self.show_url)
    #show_url.short_description = 'Link'
    #show_url.allow_tags = True
    
