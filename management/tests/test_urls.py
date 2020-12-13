from django.test import SimpleTestCase
from django.urls import reverse, resolve
from management.views import signupuser, loginuser, logoutuser, myprofile, updateprofile



class TestUrls(SimpleTestCase):
    
    def test_signupuser_urls(self):
        url = reverse('management:signupuser')
        self.assertEquals(resolve(url).func, signupuser)
        
    def test_loginuser_urls(self):
        url = reverse('management:loginuser')
        self.assertEquals(resolve(url).func, loginuser)
        
    def test_logoutuser_urls(self):
        url = reverse('management:logoutuser')
        self.assertEquals(resolve(url).func, logoutuser)
        
    def test_myprofile_urls(self):
        url = reverse('management:myprofile')
        self.assertEquals(resolve(url).func, myprofile)
        
    def test_updateprofile_urls(self):
        url = reverse('management:updateprofile')
        self.assertEquals(resolve(url).func, updateprofile)
        

