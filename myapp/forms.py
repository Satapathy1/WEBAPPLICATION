from .models import Upload_Image
from django import forms



class IMAGE_UPLOAD(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = ['image']