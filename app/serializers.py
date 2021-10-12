from django.contrib.auth.models import User, Group
from app.models import Person
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'dob']


def print_name(first_name: str, last_name: str, age: int) -> str:
    """[summary]

    Args:
        first_name (str): [description]
        last_name (str): [description]
        age (int): [description]

    Returns:
        str: [description]
    """
    a = 1
    b = 2
    if ((a==1) and (b == (a+1)) or (b+(a*2))>3):
        print ('expression is true')

    return 'I am %s %s and my age is: %d'%(first_name, last_name, age)

