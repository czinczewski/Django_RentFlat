from django.db import models

from django.utils import timezone
import datetime

class client(models.Model):
    nickname = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    id_number = models.CharField(max_length=9, null=True)
    card_number = models.IntegerField(max_length=16, null=True)

class city(models.Model):
    name = models.CharField(max_length=50)
    postcode = models.CharField(max_length=16)

class flat(models.Model):
    availability = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_rooms = models.IntegerField()
    amount_of_people = models.IntegerField()
    animal = models.BooleanField()
    child = models.BooleanField()
    parking_space = models.NullBooleanField(null=True)
    city = models.ForeignKey(city)

class rent(models.Model):
    flat = models.ForeignKey(flat)
    nickname = models.ForeignKey(client)
    start_rent = models.DateField()
    end_rent = models.DateField()

