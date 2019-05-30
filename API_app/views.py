from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from API_app.serializer import *


class AircraftsDataView(viewsets.ModelViewSet):
    queryset = AircraftsData.objects.all()
    serializer_class = AircraftsDataSerializers


class AirportsDataView(viewsets.ModelViewSet):
    queryset = AirportsData.objects.all()
    serializer_class = AirportsDataSerializers


@api_view(['GET', 'PUT', 'DELETE'])
def ticket_flights_view(request, ticket_no, flight):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ticket_flights = get_object_or_404(TicketFlights, ticket_no=get_object_or_404(Tickets,
                                                                                      ticket_no=ticket_no),
                                           flight=get_object_or_404(Flights,
                                                                    flight_id=flight))
    except BoardingPasses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TicketFlightsSerializers(ticket_flights)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            tickets = Tickets.objects.get(ticket_no=request.data["ticket_no"])
            flight = Flights.objects.get(flight_id=request.data["flight"])
            ticket_flights = TicketFlights(ticket_no=tickets, flight=flight,
                                           fare_conditions=request.data["fare_conditions"],
                                           amount=request.data["amount"])
            TicketFlights.objects.get(ticket_no=tickets, flight=flight).delete()
            ticket_flights.save()

            print("void PUT after save()")
            return Response(request.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ticket_flights.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def ticket_flights_list_view(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        print("Get all")
        queryset = TicketFlights.objects.all()
        # queryset = queryset[0:10]
        serializer = TicketFlightsSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            tickets = Tickets.objects.get(ticket_no=request.data["ticket_no"])
            flight = Flights.objects.get(flight_id=request.data["flight"])
            ticket_flights = TicketFlights(ticket_no=tickets, flight=flight,
                                           fare_conditions=request.data["fare_conditions"],
                                           amount=request.data["amount"])

            ticket_flights.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class BookingsView(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializers


@api_view(['GET', 'PUT', 'DELETE'])
def seats_view(request, aircraft_code, seat_no):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        seats = get_object_or_404(Seats, aircraft_code=get_object_or_404(AircraftsData,
                                                                         aircraft_code=aircraft_code),
                                  seat_no=seat_no)
    except BoardingPasses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SeatsSerializers(seats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            aircraft_data = get_object_or_404(AircraftsData, aircraft_code=request.data["aircraft_code"])
            seats = Seats(aircraft_code=aircraft_data, seat_no=request.data["seat_no"],
                          fare_conditions=request.data["fare_conditions"])
            Seats.objects.get(aircraft_code=aircraft_data, seat_no=request.data["seat_no"]).delete()
            seats.save()
            return Response(request.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        seats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def seats_list_view(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        queryset = Seats.objects.all()
        # queryset = queryset[0:10]
        serializer = SeatsSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            aircraft_data = get_object_or_404(AircraftsData, aircraft_code=request.data["aircraft_code"])

            seats = Seats(aircraft_code=aircraft_data, seat_no=request.data["seat_no"],
                          fare_conditions=request.data["fare_conditions"])

            seats.save()
            print("Post Seats save")
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class TicketsView(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializers


class FlightsView(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializers


@api_view(['GET', 'PUT', 'DELETE'])
def boarding_passes_view(request, ticket_no, flight_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        boarding_passes = get_object_or_404(BoardingPasses,
                                            ticket_no=get_object_or_404(TicketFlights,
                                                                        ticket_no=get_object_or_404(Tickets,
                                                                                                    ticket_no=ticket_no),
                                                                        flight_id=flight_id),
                                            flight_id=flight_id)
    except BoardingPasses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoardingPassesSerializers(boarding_passes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            ticket = get_object_or_404(Tickets, ticket_no=request.data["ticket_no"])
            tickets_flight = get_object_or_404(TicketFlights, ticket_no=ticket, flight_id=request.data["flight_id"])
            boarding_passes = BoardingPasses(ticket_no=tickets_flight, flight_id=request.data["flight_id"],
                                             boarding_no=request.data["boarding_no"], seat_no=request.data["seat_no"])
            BoardingPasses.objects.get(ticket_no=tickets_flight, flight_id=request.data["flight_id"]).delete()
            boarding_passes.save()
            return Response(request.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        boarding_passes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def boarding_passes_list_view(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        queryset = BoardingPasses.objects.all()
        # queryset = queryset[0:10]
        serializer = BoardingPassesSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            ticket = get_object_or_404(Tickets, ticket_no=request.data["ticket_no"])
            tickets_flight = get_object_or_404(TicketFlights, ticket_no=ticket, flight_id=request.data["flight_id"])
            boarding_passes = BoardingPasses(ticket_no=tickets_flight, flight_id=request.data["flight_id"],
                                             boarding_no=request.data["boarding_no"], seat_no=request.data["seat_no"])
            boarding_passes.save()
            serializer = BoardingPassesSerializers(boarding_passes, many=True)
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
