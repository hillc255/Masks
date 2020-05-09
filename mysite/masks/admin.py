from django.contrib import admin
from .models import Title
from django.utils.html import format_html
from django.utils.safestring import mark_safe


# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'materials', 'resource_link', 'update', 'image', 'image_tag',]
    readonly_fields = ('update', 'image_tag',)


    #def show_link(self, obj):
        #return '<a href="%s">Source Link</a>' % obj.get_absolute_url()
    #show_link.allow_tags = True

        #url = show_url
        #return mark_s<a href='%s'>Source Link</a>" % obj.show_url)
    
   # show_url.allow_tags = True

        #if obj.show_url:
            #return "<a href='%s'>Source Link</a>" % obj.show_url
        #else:
            #return ''
                
admin.site.register(Title, TitleAdmin)
