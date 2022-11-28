from django import forms

from mainapp import models

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ['title', 'description', 'release_date']