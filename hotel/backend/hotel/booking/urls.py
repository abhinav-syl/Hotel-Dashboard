from posixpath import basename
from django.urls import path, include
from .views import (
    BookingApiView,
    UserView,
    RoomView,
    UserLoginView,
    UserLoggedView,
    BookingListApiView,
    UserListView,
    AccountView,
)

urlpatterns = [
    path('api/book', BookingApiView.as_view(), name='booked'),
    path('api/room', RoomView.as_view(), name='Room_id'),
    path('api/user', UserView.as_view(), name='user_id'),
    path('api/user/<int:pk>', UserView.as_view(), name='user_details'),
    path('api/login', UserLoginView.as_view(), name='user_login'),
    path('api/logged', UserLoggedView.as_view(), name='user_logged'),
    path('api/bookings/<str:checkin>/<str:checkout>', BookingListApiView.as_view(), name='user_bookings'),
    path('api/accounts', AccountView.as_view(), name='user_accounts'),
    #path('', include(router.urls)),
]
