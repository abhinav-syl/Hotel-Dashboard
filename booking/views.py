from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import datetime
from .models import Booking, RoomType, Users, Room, Account
from .serializers import BookingSerializer, UserSerializer, RoomSerializer, AccountSerializer

class BookingListApiView(APIView):
    def get(self, request, checkin, checkout, *args, **kwargs):
        checkin = datetime.datetime.strptime(checkin, "%Y-%m-%d")
        checkin = datetime.datetime.date(checkin)
        print("checkin =", checkin)
        checkout = datetime.datetime.strptime(checkout, "%Y-%m-%d")
        checkout = datetime.datetime.date(checkout)
        print('chekcout = ', checkout)
        bookings = Booking.objects.filter(checkin__gte=checkin, checkout__lte=checkout)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)
class BookingApiView(APIView):
    # add permission to check if user is authenticated
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Booking.objects.all()
        serializer = BookingSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        type = request.data.get('type')
        roomType = RoomType.objects.filter(type=type)
        print(roomType)
        rooms = Room.objects.filter(available=True,type=roomType[0].id)
        print('results = ',rooms)
        if not rooms:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        room = Room.objects.filter(id=rooms[0].id)
        print('room[0] = ',room[0].type)
        price = roomType[0].cost
        time = request.data.get('time')
        print("price = ", price)
        TotalPrice = int(time)*price
        name = Users.objects.filter(name=request.data.get('name'))
        checkin = request.data.get('checkin')
        checkin = datetime.datetime.strptime(checkin, "%Y-%m-%d")
        checkin = datetime.datetime.date(checkin)
        date_temp = checkin
        checkout = request.data.get('checkout')
        checkout = datetime.datetime.strptime(checkout, "%Y-%m-%d")
        checkout = datetime.datetime.date(checkout)
        accounts = Account.objects.all()
        while (date_temp<=checkout):
            account = Account.objects.filter(date=date_temp)
            print(account)
            if not account:
                acc = {
                    'date': date_temp,
                    'income': price,
                }
                serializer = AccountSerializer(data=acc)
                if serializer.is_valid():
                    serializer.save()
                    print('serizalier account = ', serializer.data)
            account = Account.objects.filter(date=date_temp)
            account[0].income = account[0].income + price
            print(account[0].income, ' = ', account[0].income, ' + ' ,price)
            print(account[0].income)
            account.update(income=account[0].income)
            print(date_temp)
            date_temp = date_temp + datetime.timedelta(days=1)
            room.update(available=False)
        data = {
            'checkout': request.data.get('checkout'), 
            'checkin': request.data.get('checkin'), 
            #'user': request.user.id
            'room': room[0].id,
            'heads': request.data.get('heads'),
            'name': name[0].id,
            'type': roomType[0].id,
            'price': price,
            'totalPrice': TotalPrice,
            'time': time,
        }
        accounts = Account.objects.all()
        print(data)
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# create class for Room
class RoomView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'available': request.data.get('available'), 
            'type': request.data.get('type'), 
            # 'user': request.user.id
        }
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'),
            'username': request.data.get('username'),
            'password' : request.data.get('password'),
            # 'completed': request.data.get('type'), 
            # 'user': request.user.id
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = Users.objects.filter(username=request.data.get('username'), password=request.data.get('password'))
        #username = Users.objects.all()
        username.update(logged=True)
        serializer = UserSerializer(username, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLoggedView(APIView):
    def get(self, request, *args, **kwargs):
        username = Users.objects.filter(logged=True)
        #username = Users.objects.all()
        serializer = UserSerializer(username, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(APIView):
    def get(self, request, pk, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        users = Users.objects.filter(id=pk)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccountView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
