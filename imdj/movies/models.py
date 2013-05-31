#-*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


__all__ = ['Actor', 'Director', 'Movie']


class BasePerson(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='photos')
    bio = models.TextField()
    date_of_birth = models.DateTimeField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

    class Meta:
        abstract = True


class Actor(BasePerson):

    def get_absolute_url(self):
        return reverse('actor_detail', args=(self.pk, self.slug))


class Director(BasePerson):

    prizes = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('director_detail', args=(self.pk, self.slug))


class Movie(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField()
    director = models.ForeignKey(Director)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie_list', args=(self.pk, self.slug))

    class Meta:
        ordering = ('likes',)


def create_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(create_slug, sender=Movie)
