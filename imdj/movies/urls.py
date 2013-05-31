from django.conf.urls import patterns, url


urlpatterns = patterns(
    'imdj.movies.views',
    url(r'^$', 'movie_list', name='movie_list'),
    url(r'^suggest/$', 'suggest', name='suggest'),
    url(r'^actor/(?P<pk>\d+)/(?P<slug>[^/]/$', 'actor_detail', name='actor_detail'),
    url(r'^director/(?P<pk>\d+)/(?P<slug>[^/]/$', 'director_detail', name='director_detail')
)
