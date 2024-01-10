from django.contrib import admin
from .models import Upload_Image


@admin.register(Upload_Image)
class Upload_ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'image_type')
    list_filter = ('image_type',)

