from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','author','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'author': forms.TextInput(attrs={'class':'form-control','placeholder':'Author','id':'elder'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('title','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
        }


