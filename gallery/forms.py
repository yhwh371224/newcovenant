from .models import Comment, Gallery
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('name', 'title', 'content')        
    
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
