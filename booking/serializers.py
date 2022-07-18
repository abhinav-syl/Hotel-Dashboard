from rest_framework import serializers

from .models import Booking, Users, Room, Account

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','name','checkin','checkout','heads','room','type','price','time','totalPrice']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'username','logged','state']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = ['id','available','type']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['date','income']