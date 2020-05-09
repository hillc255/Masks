from django.contrib import admin
from .models import Title


# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'materials', 'link', 'update', 'image', 'image_tag',]
    readonly_fields = ('update', 'image_tag',)
    list_filter = ('title', 'update',)
    date_heirarchy = 'pub_date'
    ordering = ('-pub_date',)


admin.site.register(Title, TitleAdmin)
