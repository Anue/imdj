#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from imdj.movies.models import Actor, Director, Movie
from imdj.movies.forms import MovieForm


def movie_list(request):
    render(request, "imdj/movie_list.html", {
        'movie_set': Movie.objects.all()
    })


def _detail(request, template, Model, pk, slug):
    obj = get_object_or_404(Model, pk=pk, slug=slug)
    return render(request, template, {
        'object': obj
    })


def actor_detail(request, pk=None, slug=None):
    return _detail(request, "imdj/actor_detail.html", Actor, pk, slug)


def director_detail(request, pk=None, slug=None):
    return _detail(request, "imdj/director_detail.html", Director, pk, slug)


def suggest(request, template="imdj/suggest.html"):
    form = MovieForm(request.Post or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movies:movie_list'))
    return render(request, template, {
        'form': form
    })
