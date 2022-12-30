from rest_framework import serializers
from .models import Guest,Movie,Reservations

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
      class Meta:
        model=Reservations
        fields='__all__'


class GuestSerializer(serializers.ModelSerializer):
      class Meta:
        model=Guest
        fields=['pk','name','mobile','reservation']       