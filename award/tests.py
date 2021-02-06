from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        '''
        run before test
        '''
        user1=User(username='missy')
        user1.save()
        self.profile1=Profile(user=user1,bio='kid livin life',email='ngam@gmail.com')

    def test_instance(self):
        '''
        test profile object initialization 
        '''
        self.assertTrue(isinstance(self.profile1,Profile))


    def test_save(self):
        '''
        test profile save 
        '''
        self.profile1.save()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>=1)

