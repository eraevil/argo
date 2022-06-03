# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Argometa(models.Model):
    platformnumber = models.IntegerField(primary_key=True)
    transmissionsys = models.CharField(max_length=8, blank=True, null=True)
    postioningsys = models.CharField(max_length=16, blank=True, null=True)
    platformodel = models.CharField(max_length=16, blank=True, null=True)
    platformaker = models.CharField(max_length=30, blank=True, null=True)
    firmwareversion = models.CharField(max_length=32, blank=True, null=True)
    serialnumber = models.CharField(max_length=32, blank=True, null=True)
    manualversion = models.CharField(max_length=16, blank=True, null=True)
    instrumentype = models.CharField(max_length=3, blank=True, null=True)
    projectname = models.CharField(max_length=64, blank=True, null=True)
    datacentre = models.CharField(max_length=2, blank=True, null=True)
    piname = models.CharField(max_length=60, blank=True, null=True)
    startupdate = models.CharField(max_length=14, blank=True, null=True)
    launchdate = models.CharField(max_length=14, blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    deployplatform = models.CharField(max_length=40, blank=True, null=True)
    parkpressure = models.IntegerField(blank=True, null=True)
    profilepressure = models.IntegerField(blank=True, null=True)
    platformstatus = models.IntegerField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'argometa'

class Targoheader(models.Model):
    platformname = models.CharField(max_length=255, blank=True, null=True)
    cyclenumber = models.CharField(max_length=255, blank=True, null=True)
    sampledirection = models.CharField(max_length=255, blank=True, null=True)
    datamode = models.CharField(max_length=255, blank=True, null=True)
    julianday = models.CharField(max_length=255, blank=True, null=True)
    datadate = models.CharField(max_length=255, blank=True, null=True)
    qc4date = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    qc4location = models.CharField(max_length=255, blank=True, null=True)
    creationdate = models.CharField(max_length=255, blank=True, null=True)
    updatedate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'targoheader'

class Argocore(models.Model):
    platformnumber = models.IntegerField(blank=True, null=True)
    cyclenumber = models.IntegerField(blank=True, null=True)
    pressure = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    cpressure = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    qpressure = models.CharField(max_length=1, blank=True, null=True)
    temperature = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    ctemperature = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    qtemperature = models.CharField(max_length=1, blank=True, null=True)
    salinity = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    csalinity = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    qsalinity = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argocore'



