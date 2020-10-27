from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Dog(models.Model):
    GENDER_LIST = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    COLOR_LIST = (
        ('WT', 'White'),
        ('BK', 'Black'),
        ('BN', 'Brown'),
    )

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    color = models.CharField(max_length=2, choices=COLOR_LIST)
    favoritefood = models.CharField(max_length=50, blank=True)
    favoritetoy = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.breed) + ' ' + str(self.get_gender_display())

class Breed(models.Model):
    SIZE_LIST = (
        ('T', 'Tiny'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=SIZE_LIST)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.name) + ' ' + str(self.get_size_display())
