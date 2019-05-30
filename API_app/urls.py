from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from API_app.views import *

router = routers.DefaultRouter()
router.register("aircrafts_data", AircraftsDataView)
router.register("airports_data", AirportsDataView)
router.register("bookings", BookingsView)
router.register("flights", FlightsView)
router.register("tickets", TicketsView)

urlpatterns = [
    path('boarding_passes/<slug:ticket_no>/<int:flight_id>/', boarding_passes_view, name="boarding_passes"),
    path('boarding_passes/', boarding_passes_list_view, name="boarding_passes_list"),
    path('seats/<slug:aircraft_code>/<slug:seat_no>/', seats_view, name="seats"),
    path('seats/', seats_list_view, name="seats_list"),
    path('ticket_flights/<slug:ticket_no>/<int:flight>/', ticket_flights_view, name="ticket_flights"),
    path('ticket_flights/', ticket_flights_list_view, name="ticket_flights_list"),
    path('base_auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
    path('', include(router.urls))
]
