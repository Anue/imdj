#-*- coding: utf-8 -*-

from datetime import date

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

    def get_age(self):
        if self.date_of_birth is None:
            return None
        today = date.today()
        try:
            birthday = self.date_of_birth.replace(year=today.year)
        except ValueError:
            # Birth date is February 29 and it's not on a leap year
            birthday = self.date_of_birth.replace(
                year=today.year, day=self.date_of_birth.day - 1)
        if birthday > today:
            age = today.year - self.date_of_birth.year - 1
        else:
            age = today.year - self.date_of_birth.year
        if age > 0:
            return age

    class Meta:
        abstract = True


class Actor(BasePerson):

    def get_absolute_url(self):
        return reverse('movies:actor_detail', args=(self.pk, self.slug))


class Director(BasePerson):

    prizes = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('director_detail', args=(self.pk, self.slug))


class Movie(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers')
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
        return reverse('movies:movie_detail', args=(self.pk, self.slug))

    class Meta:
        ordering = ('likes',)


def create_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(create_slug, sender=Movie)
