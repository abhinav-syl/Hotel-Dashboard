from django.contrib import admin

# Register your models here.
from .models import Booking, Users, Room, RoomType, UserPassword, Account
admin.site.register(Booking)
admin.site.register(Users)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(UserPassword)
admin.site.register(Account)