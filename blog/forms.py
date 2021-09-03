from django import forms


class PostForm(forms.Form):
    title=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    slug=forms.SlugField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))