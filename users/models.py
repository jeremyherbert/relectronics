from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	studentNum = models.CharField(max_length=8)
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.user.__unicode__()

#save profile on create
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        #add the intial points transaction (Later)

post_save.connect(create_user_profile, sender=User)