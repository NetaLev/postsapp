from django import forms
from .models import Post


class PostForm(forms.ModelForm):

# category = forms.ChoiceField(choices=[(doc.uid, doc.name) for doc in Document.objects.all()])
    class Meta:
        model = Post
        fields = ('category', 'post',)
