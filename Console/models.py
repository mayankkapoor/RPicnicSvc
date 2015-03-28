from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20)
    phone_number = models.IntegerField()

class Depot(models.Model):
    depot_number = models.IntegerField();
    depot_address = models.CharField(max_length=1000)

class Bus(models.Model):
    bus_number = models.CharField(max_length=20)
    bus_driver = models.ForeignKey(Person)
    bus_depot = models.ForeignKey(Depot)
