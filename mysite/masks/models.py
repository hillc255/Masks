import os.path
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.

class Title(models.Model):
    title = models.CharField(max_length=300)
    materials = models.CharField(max_length=800,blank=True)
    link = models.URLField(
            max_length=150,
            db_index=True,
            unique=True,
            blank=True
    )
    name = models.CharField(max_length=50,blank=True)
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
    image_tag.short_description = 'Image'

    def __unicode__(self):
        return self.title
    
    #def image(self):
     #   from django.utils.html import escape
      #  return u'<img src="%s" />' % self.image.url_123x123 
        #escape("/media/images")
    #image.short_description = 'Image'
    
