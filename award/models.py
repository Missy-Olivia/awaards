from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models import Q

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =models.ImageField(upload_to= 'profiles/', blank=True, default='profiles/default.png')
    bio = models.CharField(max_length=500, default='No bio')
    email=models.EmailField(default='No email')
    contact = models.CharField(max_length=80)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio)
        return update_profile
