from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Cource(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.CharField(max_length=124)
    age = models.CharField(max_length=124)
    gender = models.CharField(max_length=124)
    Phone = models.CharField(max_length=124)
    address = models.CharField(max_length=124)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    cource = models.ForeignKey(Cource, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, blank=True, null=True)
   
    def __str__(self):
        return self.name