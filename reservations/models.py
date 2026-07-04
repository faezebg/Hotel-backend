from django.db import models
from django.core.exceptions import ValidationError

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.city})"

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.hotel.name}"


class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")

    def __str__(self):
        return f"{self.customer_name} - {self.room}"

    def clean(self):
        overlapping = Reservation.objects.filter(
            room=self.room,
            check_in__lt=self.check_out,
            check_out__gt=self.check_in
        )

        if overlapping.exists():
            raise ValidationError("This room is already reserved in this date range")

    def save(self, *args, **kwargs):
        self.clean()
        self.room.is_available = False
        self.room.save()
        super().save(*args, **kwargs)
