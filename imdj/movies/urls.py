from django.conf.urls import patterns, url


urlpatterns = patterns(
    'imdj.movies.views',
    url(r'^$', 'movie_list', name='movie_list'),
    url(r'^suggest/$', 'suggest', name='suggest'),
    url(r'^actor/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        'actor_detail', name='actor_detail'),
    url(r'^movie/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        'movie_detail', name='movie_detail'),
    url(r'^director/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        'director_detail', name='director_detail'),
    url(r'^like/$', 'ajax_like', name='ajax_like')
)
