import os.path
from datetime import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.

class Title(models.Model):
    EASY = 'Easy'
    OK = 'OK'
    HARD = 'Hard'
    LEVEL_CHOICES = [
            (EASY, 'Easy'),
            (OK, 'OK'),
            (HARD, 'Hard'),
    ]        
    title = models.CharField(max_length=300)
    materials = models.CharField(max_length=800,blank=True)
    resource = models.URLField(max_length=150,blank=True)
    level = models.CharField(max_length=6,choices=LEVEL_CHOICES, default=EASY,)
    update = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/noimage.gif')
    pub_date = models.DateTimeField('date published', null=True)
   
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
   
    def url(self):
        return os.path.join('/',settings.MEDIA_URL, "images", os.path.basename(str(self.image)))

    def image_tag(self):
        return mark_safe('<img src="{}" width="80" height="80" />'.format(self.url()) )
    image_tag.short_description = 'Thumbnail'

    def link(self):
        return mark_safe('<a href="{}">Resource</a>'.format(self.resource) )
    link.allow_tags = True
