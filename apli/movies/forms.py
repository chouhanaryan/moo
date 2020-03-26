from .models import Movie, Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'youtube_id')
        labels = {'youtube_id': 'YouTube ID'}