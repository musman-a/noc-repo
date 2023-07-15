from django.db import models
from datetime import date

# Create your models here.

class Icccomplaints(models.Model):
    tokenid = models.CharField(max_length=50, primary_key=True)
    clientname = models.CharField(max_length=50)
    typeofcomplaint = models.CharField(max_length=100)
    complaintlevel = models.CharField(max_length=100, default="L1")
    status = models.CharField(max_length=50, default="Pending")
    date = models.DateField()

def __str__(self):
    return self.clientname

class Ncdcomplaints(models.Model):
    tokenid = models.CharField(max_length=50, primary_key=True)
    clientname = models.CharField(max_length=50)
    typeofcomplaint = models.CharField(max_length=100)
    complaintlevel = models.CharField(max_length=100, default="L1")
    status = models.CharField(max_length=50, default="Pending")
    date = models.DateField()

def __str__(self):
    return self.username


class Seacomplaints(models.Model):
    tokenid = models.CharField(max_length=50, primary_key=True)
    clientname = models.CharField(max_length=50)
    typeofcomplaint = models.CharField(max_length=100)
    complaintlevel = models.CharField(max_length=100, default="L1")
    status = models.CharField(max_length=50, default="Pending")
    date = models.DateField()

def __str__(self):
    return self.username


class Cccomplaints(models.Model):
    tokenid = models.CharField(max_length=50, primary_key=True)
    clientname = models.CharField(max_length=50)
    typeofcomplaint = models.CharField(max_length=100)
    complaintlevel = models.CharField(max_length=100, default="L1")
    status = models.CharField(max_length=50, default="Pending")
    date = models.DateField()

def __str__(self):
    return self.username


class Acscomplaints(models.Model):
    tokenid = models.CharField(max_length=50, primary_key=True)
    clientname = models.CharField(max_length=50)
    typeofcomplaint = models.CharField(max_length=100)
    complaintlevel = models.CharField(max_length=100, default="L1")
    status = models.CharField(max_length=50, default="Pending")
    date = models.DateField()

def __str__(self):
    return self.username


class Sqcomplaints(models.Model):
    tokenid = models.CharField(max_length=50, primary_key=True)
    clientname = models.CharField(max_length=50)
    typeofcomplaint = models.CharField(max_length=100)
    complaintlevel = models.CharField(max_length=100, default="L1")
    status = models.CharField(max_length=50, default="Pending")
    date = models.DateField()

def __str__(self):
    return self.username

    
                        


