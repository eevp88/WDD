from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    user = models.OneToOneField(User)
    class Meta:
	ordering=["id"]
	verbose_name_plural = "UserProfiles"    

    def __str__(self):
        return self.user.username
