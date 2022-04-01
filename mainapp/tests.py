from rest_framework.test import APITestCase
from django.urls import reverse


class UserTestCase(APITestCase):
    def setUp(self):
        data = {"username": "admin", "password": "admin", "is_doctor": True}
        self.client.post(reverse("registration"), data=data)

    def test_autherization(self):
        data = {"username": "admin", "password": "admin"}
        response = self.client.post(reverse("token_obtain_pair"), data=data)
        self.assertEqual(200, response.status_code)
        
        
class PacientTestCase(APITestCase):
    def setUp(self):
        data = {'username': 'admin', 'password': 'admin', "is_doctor": True}
        auth_data = {'username': 'admin', 'password': 'admin', "is_doctor": True}
        
        diagnoses = {"name_diagnos": "Diagnos name"}
        diagnoses2 = {"name_diagnos": "Diagnos name2"}
        
        pacient = { "date_of_birth": "2017-01-01", "diagnoses": [1, 2] }
        pacient2 = { "date_of_birth": "2017-01-01", "diagnoses": [2] }
        pacient3 = { "date_of_birth": "2017-01-01", "diagnoses": [1] }
        
        self.client.post(reverse('registration'), data=data)
        self.token = self.client.post(
            reverse('token_obtain_pair'), data=auth_data).json().get('access')
        
        self.client.post(reverse('diagnos-list'), data=diagnoses)
        self.client.post(reverse('diagnos-list'), data=diagnoses2)
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        self.client.post(reverse('pacient-list'), data=pacient)
        self.client.post(reverse('pacient-list'), data=pacient2)
        self.client.post(reverse('pacient-list'), data=pacient3)

    def test_create_post(self):
        response = self.client.get(reverse('pacient-list'))
        self.assertEqual(200, response.status_code)
