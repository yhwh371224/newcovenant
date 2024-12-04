from .models import Gallery
from django import forms


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'date', 'head_image')        
    
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['readonly'] = True
        self.fields['date'].widget.attrs['class'] = 'datepicker' 
