from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)
    spotify_uri = models.CharField(max_length= 100, primary_key = True)

    def __str__(self):
        return self.spotify_uri
