from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins

from app.models import Person
from app.serializers import PersonSerializer

class PersonViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
                
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
