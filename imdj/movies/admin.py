#-*- coding: utf-8 -*-

from django.contrib import admin
from imdj.movies.models import Actor, Director, Movie


class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}


class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)
}

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
