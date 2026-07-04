from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home,
    HotelViewSet,
    RoomViewSet,
    ReservationViewSet,
    HotelListView,
    RoomDetailView
)

router = DefaultRouter()
router.register(r'hotels', HotelViewSet, basename='hotel')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', home, name='home'),
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('api/', include(router.urls)),]
