#-*- coding: utf-8 -*-
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import (
    HttpResponse, HttpResponseRedirect, HttpResponseForbidden)
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from imdj.movies.models import Actor, Director, Movie
from imdj.movies.forms import MovieForm


def movie_list(request):
    movies = Movie.objects.filter(published=True)
    paginator = Paginator(movies, 5)  # Show 5 movies per page
    page = request.GET.get('page')
    try:
        movie_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movie_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movie_set = paginator.page(paginator.num_pages)
    return render(request, "imdj/movie_list.html", {
        'movie_set': movie_set
    })


def _detail(request, template, Model, pk, slug, extra=None):
    if extra is None:
        extra = {}
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


@require_POST
def ajax_like(request):
    movie = get_object_or_404(Movie, pk=request.POST.get('pk', None))
    key = 'liked_movie_{0}'.format(movie.pk)
    if request.session.get(key):
        return HttpResponseForbidden()
    movie.likes += 1
    movie.save()
    response = HttpResponse(json.dumps({
        'success': True,
        'count': movie.likes
    }), mimetype="application/json")
    response.set_cookie(key, True)
    return response
