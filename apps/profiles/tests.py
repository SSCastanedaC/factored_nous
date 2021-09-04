from django.http import response
from django.test import TestCase, Client, client
from django.contrib.auth.models import User

# Create your tests here.
#Run the test using 'python manage.py test apps.profiles.tests'

class TestFlow(TestCase):
    def test_flow(self):
        client = Client()
        #Test Login and Home
        client.login(username='sebastianc', password='factored2021')
        response_home = client.get('/profiles/home')
        assert response_home.status_code == 200
        #Test Update 
        client.post('/profiles/profile', {
            'first_name': 'Steffen',
            'last_name': 'Castillo'
        }, follow=True)
        test_user = User.objects.get(username='sebastianc')
        assert test_user.first_name == 'Steffen'
        assert test_user.last_name == 'Castillo'