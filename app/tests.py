from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Person
import datetime

import logging
logger = logging.getLogger(__name__)

class PersonViewSetTests(APITestCase):
    def add_test_person(self):
        """
        Adds a test person into the database
        """
        logger.debug('Adding a new person into database')
        p = Person(first_name='Unbiased', last_name='Coder', dob=datetime.date(2021, 9, 1))
        p.save()
        logger.debug('Successfully added test person into the database')

    def test_delete_persons(self):
        """
        Test to see if deleting works
        """
        logger.debug('Starting test delete persons')

        self.add_test_person()

        url = 'http://127.0.0.1:8000%s1/'%reverse('person-list')
        logger.debug('Sending TEST data to url: %s'%url)
        response = self.client.delete(url, format='json')

        logger.debug('Testing to see if status code is correct')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_persons(self):
        """
        Test to see if put works
        """
        logger.debug('Starting test put persons')

        self.add_test_person()

        url = 'http://127.0.0.1:8000%s1/'%reverse('person-list')
        logger.debug('Sending TEST data to url: %s'%url)
        data = {
            'first_name' : 'Unbiased11',
            'last_name'  : 'Coder11',
            'dob'        : '2021-09-01'
        }

        response = self.client.put(url, data, format='json')
        json = response.json()
        
        logger.debug('Testing to see if status code is correct')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing modified person object details')
        p = Person.objects.get()
        self.assertEqual(p.first_name, 'Unbiased11')
        self.assertEqual(p.last_name, 'Coder11')

        logger.debug('Test person put completed successfully')


    def test_list_persons(self):
        """
        Test to list all the persons in the list
        """
        logger.debug('Starting test list persons')

        self.add_test_person()

        url = 'http://127.0.0.1:8000%s'%reverse('person-list')
        logger.debug('Sending TEST data to url: %s'%url)
        response = self.client.get(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing result count')
        self.assertEqual(len(json), 1)


    def test_create_person(self):
        """
        Tests creating a new person object
        """
        logger.debug('Starting test create person')
        url = 'http://127.0.0.1:8000%s'%reverse('person-list')
        data = {
            'first_name' : 'Unbiased',
            'last_name'  : 'Coder',
            'dob'        : '2021-09-01'
        }

        logger.debug('Sending TEST data to url: %s, data: %s'%(url, data))

        response = self.client.post(url, data, format='json')
        
        logger.debug('Testing status code response: %s, code: %d'%(response.json(), response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        logger.debug('Testing person count to make sure object was successfully added')
        self.assertEqual(Person.objects.count(), 1)

        logger.debug('Testing new person object details')
        p = Person.objects.get()
        self.assertEqual(p.first_name, 'Unbiased')
        self.assertEqual(p.last_name, 'Coder')
        self.assertEqual(p.dob, datetime.date(2021, 9, 1))

        logger.debug('Test person create completed successfully')
