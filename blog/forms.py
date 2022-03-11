from dataclasses import fields
from django import forms
from blog.models import Post

class DateInput(forms.DateInput):
    input_type = "date"

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "date")
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=DateInput)
        