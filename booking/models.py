from cgi import print_arguments
from pyexpat import model
from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import IntegerField
from datetime import date

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    logged = models.BooleanField(default=False)
    state = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

class Room(models.Model):
    available = models.BooleanField(default=True)
    #type = models.CharField(max_length=30, default='single')
    type = models.ForeignKey('RoomType', on_delete = models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)


class RoomType(models.Model):
    choice = (
        ('single', 'single room'),
        ("double", "double room"),
        ("triple", "triple room"))
    type = models.CharField(max_length=30, choices=choice, default='single')
    cost = models.IntegerField(default=2500)
    def __str__(self):
        return str(self.type)


class UserPassword(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return str(self.username)

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this booking')
    checkout = models.DateField()
    checkin = models.DateField()
    name = models.ForeignKey('Users', on_delete = models.CASCADE, blank = True, null = True)
    heads = models.IntegerField(default=1)
    room = models.ForeignKey('Room', on_delete = models.CASCADE, blank = True, null = True)
    price = models.IntegerField(default=2500)
    totalPrice = models.IntegerField(default=2500)
    type = models.ForeignKey('RoomType', on_delete = models.CASCADE, blank = True, null = True)
    time = models.IntegerField(default=1)
    def __str__(self):
        return str(self.name) + str(self.room)

class Account(models.Model):
    date = models.DateField(primary_key=True, default=date.today)
    income = models.IntegerField(default=0)