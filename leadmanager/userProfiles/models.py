from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image 
from django.db.models.signals import post_save, pre_save    

User = settings.AUTH_USER_MODEL

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    #username = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
        

    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

def user_did_save(sender, instance,created ,*args, **kwargs):
    userProfile.objects.get_or_create(user=instance)
    if created:
        userProfile.objects.get_or_create(user=instance)

post_save.connect(user_did_save ,sender=User)