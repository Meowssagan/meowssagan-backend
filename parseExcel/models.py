from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Pet(models.Model):
    timestamp = models.DateTimeField()
    shelter_name = models.CharField(max_length=255)
    animal_type = models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    size = models.CharField(max_length=255)
    shelter_duration = models.FloatField() 
    medical_conditions = models.TextField(blank=True, null=True)
    vaccines = models.TextField(blank=True, null=True)
    character = models.TextField(blank=True, null=True)
    behavior = models.TextField(blank=True, null=True)
    commands = models.TextField(blank=True, null=True)
    relation_to_people = models.TextField(blank=True, null=True)
    relation_to_animals = models.TextField(blank=True, null=True)
    availability = models.CharField(max_length=255)

    def __str__(self):
        return self.pet_name
