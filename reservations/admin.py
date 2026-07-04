from django.contrib import admin
from .models import Hotel, Room, Reservation

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'stars')
    search_fields = ('name', 'city')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel', 'capacity', 'price_per_night', 'is_available')
    list_filter = ('hotel', 'is_available')
    autocomplete_fields = ('hotel',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'room', 'check_in', 'check_out')
    search_fields = ('customer_name',)
    list_filter = ('room__hotel',)
