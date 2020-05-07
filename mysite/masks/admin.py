from django.contrib import admin
from .models import Title

# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'materials', 'link', 'name', 'image', 'image_tag',)
    readonly_fields = ('image_tag',)

admin.site.register(Title, TitleAdmin)
