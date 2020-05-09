from django.contrib import admin
from .models import Title


# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'materials', 'link', 'level', 'update', 'image_tag',]
    readonly_fields = ('update', 'image_tag',)
    list_filter = ('level', 'update',)
    date_heirarchy = 'pub_date'
    ordering = ('-pub_date',)


    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'level':
            kwargs['choices'] = (
                    ('Easy', 'Easy'),
                    ('OK', 'OK'),
                    ('Hard', 'Hard'),
            )
        return super().formfield_for_choice_field(db_field, request, **kwargs)


admin.site.register(Title, TitleAdmin)
