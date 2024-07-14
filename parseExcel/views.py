from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pet
from .serializers import PetSerializer
from .filters import PetFilter

class PetListView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    renderer_classes = [JSONRenderer]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetFilter

class PetDetailView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    renderer_classes = [JSONRenderer]