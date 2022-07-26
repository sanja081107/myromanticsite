from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo')
    list_display_links = ('id', 'title')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{ object.image.url }' width=50>")

    get_html_photo.short_description = 'Миниатюра'

admin.site.register(Question)
admin.site.register(Photo, PhotoAdmin)

