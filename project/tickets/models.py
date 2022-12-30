from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token
from django.conf import settings
#Movie 
class Movie(models.Model):
    hall=models.CharField(max_length=10)
    movie=models.CharField(max_length=200)
    date=models.DateField()
#Customer
class Guest(models.Model):
    name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=15)

#Reservation
class Reservations(models.Model):
    guest=models.ForeignKey(Guest,related_name='reservation',on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,related_name='reservation',on_delete=models.CASCADE)     

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def TokenCearte(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)