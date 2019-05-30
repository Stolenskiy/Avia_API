from rest_framework import serializers

from API_app.models import *


class AircraftsDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = AircraftsData
        fields = ("aircraft_code", "model", "range")


class AirportsDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = AirportsData
        fields = ("airport_code", "airport_name", "city", "coordinates", "timezone")


class BookingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ("book_ref", "book_date", "total_amount")


class FlightsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = (
            "flight_id", "flight_no", "scheduled_departure", "scheduled_arrival", "departure_airport",
            "arrival_airport",
            "status", "aircraft_code", "actual_departure", "actual_arrival")


class SeatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ("aircraft_code", "seat_no", "fare_conditions")


class TicketFlightsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TicketFlights
        fields = ("ticket_no", "flight", "fare_conditions", "amount")


class BoardingPassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = BoardingPasses
        fields = ("ticket_no", "flight_id", "boarding_no", "seat_no")


class TicketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ("ticket_no", "book_ref", "passenger_id", "passenger_name", "contact_data")
