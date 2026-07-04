from rest_framework import serializers
from .models import Hotel, Room, Reservation

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        room = data['room']
        check_in = data['check_in']
        check_out = data['check_out']
        if Reservation.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in
        ).exists():
            raise serializers.ValidationError("Room already reserved for this date range")
        return data
