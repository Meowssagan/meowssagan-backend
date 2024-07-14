import django_filters
from .models import Pet

class PetFilter(django_filters.FilterSet):
    class Meta:
        model = Pet
        fields = {
            'shelter_name': ['exact'],
            'animal_type': ['exact'],
            'gender': ['exact'],
            'age': ['exact', 'lte', 'gte'],  # exact match and range filters
            'size': ['exact'],
        }
