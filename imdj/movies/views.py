#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from imdj.movies.models import Actor, Director, Movie
from imdj.movies.forms import MovieForm


def movie_list(request):
    return render(request, "imdj/movie_list.html", {
        'movie_set': Movie.objects.filter(published=True)
    })


def _detail(request, template, Model, pk, slug, extra={}):
    obj = get_object_or_404(Model, pk=pk, slug=slug, **extra)
    return render(request, template, {
        'object': obj
    })


def actor_detail(request, pk=None, slug=None):
    return _detail(request, "imdj/actor_detail.html", Actor, pk, slug)


def director_detail(request, pk=None, slug=None):
    return _detail(request, "imdj/director_detail.html", Director, pk, slug)


def movie_detail(request, pk=None, slug=None):
    return _detail(request, "imdj/movie_detail.html",
                   Movie, pk, slug,
                   extra={'published': True})


def suggest(request, template="imdj/suggest.html"):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movies:movie_list'))
    return render(request, template, {
        'form': form
    })
