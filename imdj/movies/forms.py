#-*- coding: utf-8 -*-

from django import forms
from imdj.movies.models import Movie


__all__ = ['MovieForm']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('published', 'slug', 'likes')
