from django.db import models

class main_area(models.Model):
    name = models.CharField(max_length=64)
    channel = models.ManyToManyField('infochannel')
    format = models.ForeignKey('format')

class format(models.Model):
    name = models.CharField(max_length=64)
    orientation = models.BooleanField()
    size = models.IntegerField()

class infochannel(models.Model):
    name = models.CharField(max_length=64)

class message(models.Model):
    headline = models.CharField(max_length=64)
    text = models.TextField()
    channel = models.ForeignKey('infochannel')