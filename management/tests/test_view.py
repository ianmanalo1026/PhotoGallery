from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.contrib.auth.models import User
from management.models import Profile
from django.urls import reverse



class TestView(TestCase):
    
    def setUp(self) -> None:
        self.credentials = {
            'username': 'testuser1234',
            'password': 'password1234'
        }
        self.create1 = {
            'username': 'test12345',
            'first_name': 'test12345',
            'last_name': 'test12345',
            'email': 'test@email.com',
            'password1': 'test12345',
            'password2': 'test12345',
        }
        User.objects.create_user(**self.credentials)
        client = Client()
        
    def test_login(self):
        response = self.client.post('/loginuser/', 
                                    self.credentials, 
                                    follow=True
                                    )
        self.assertTrue(response.context['user'].is_authenticated)
        
    def test_logoutuser(self):
        response = self.client.post('/logoutuser/',
                                    self.credentials,
                                    follow=True
                                    )
        self.assertEqual(response.status_code, 200)
        
    def test_signupuser(self):
        response = self.client.post(reverse('management:signupuser'),
                                    self.create1
                                    )
        
        self.assertEqual(self.create1['password1'],
                         self.create1['password2']
                         )
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(),1)
        
    def test_myprofile_view(self):
        response = self.client.get(reverse('management:myprofile'), follow=True)
        
        self.assertEqual(response.status_code, 200)
        
    def test_updateprofile_view(self):
        login = self.client.post('/loginuser/', 
                                    self.credentials, 
                                    follow=True
                                    )
        
        response = self.client.get(reverse('management:updateprofile'), follow=True)

        self.assertTrue(login.context['user'].is_authenticated)
        self.assertTrue(login.status_code, 200)
        self.assertEqual(response.status_code, 200)
        
         