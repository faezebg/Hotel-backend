from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from rest_framework.viewsets import ModelViewSet

from .models import Hotel, Room, Reservation
from .serializers import HotelSerializer, RoomSerializer, ReservationSerializer


def home(request):
    return HttpResponse("Backend project is running successfully")


class HotelListView(ListView):
    model = Hotel
    template_name = "reservations/hotel_list.html"
    context_object_name = "hotels"

class RoomDetailView(DetailView):
    model = Room
    template_name = "reservations/room_detail.html"
    context_object_name = "room"

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
