from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
