from django import forms
from tinymce import TinyMCE
from .models import Posting, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Posting
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type your Comment',
        'id':'usercomment',
        'rows':'4'

        }))
    class Meta:
        model = Comment
        fields = ('content',)

class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))

