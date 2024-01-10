from django.db import models

# Create your models here.


class Upload_Image(models.Model):
    image = models.ImageField(upload_to='images')
    image_type = models.CharField(max_length=70, choices=(('portrait','portrait'),('Landscape','Landscape')))