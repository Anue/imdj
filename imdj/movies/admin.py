#-*- coding: utf-8 -*-

from django.contrib import admin
from imdj.movies.models import Actor, Director, Movie


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    # list_display = ('first_name', 'last_name', 'date_of_birth')


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # list_display = ['name', 'year', 'published']
    # list_filter = ('published', 'year')

admin.site.register(Actor, PersonAdmin)
admin.site.register(Director, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
