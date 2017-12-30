from __future__ import unicode_literals

from django.db import models

class Brand(models.Model):
    brandId = models.IntegerField(default=0)
    brandName = models.TextField(default="")
    modelName = models.TextField(default="")
    versionName = models.TextField(default="")
    link = models.TextField(default="")

# class Link(models.Model):
#     linkId = models.IntegerField(default=0)
#     brId = models.ForeignKey(Brand, default=None)
#     time = models.TimeField()
#     link = models.TextField(default="")
#     parsed = models.BooleanField(default=False)
#
# class InvalidLink(models.Model):
#     linkId = models.IntegerField(default=0)
#     time = models.TimeField()
#     linkText = models.TextField(default="")
#     parsed = models.BooleanField(default=False)
#
# class Car(models.Model):
#     bId = models.ForeignKey(Brand, default=None)
#     lId = models.ForeignKey(Link, default=None)
#
#     year = models.IntegerField(default=0)
#     mileage = models.IntegerField(default=0)
#     power = models.IntegerField(default=0)
#     capacity = models.IntegerField(default=0)
#     fuel = models.TextField(default=0)
#     color = models.TextField(default=0)
#     usedOrNew = models.TextField(default=0)
#     doors = models.TextField(default=0)
#     gearBox = models.TextField(default=0)
#
#     price = models.IntegerField(default=0)


# Create your models here.
