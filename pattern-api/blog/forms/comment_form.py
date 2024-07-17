from django import forms


class CommentForm(forms.Form):
    title = forms.CharField(max_length=200)
    username = forms.CharField(max_length=255)
    comment = forms.CharField(widget=forms.Textarea)
