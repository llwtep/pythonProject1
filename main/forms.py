from .models import Post
from django.contrib.auth.forms import forms


class PostCreateForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Title'
        })
    )
    content = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Content'
        })
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']

    def save(self, commit=True, user=None):
        post = super().save(commit=False)
        if user:
            post.author = user
        if commit:
            post.save()
        return post

