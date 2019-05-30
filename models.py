# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AircraftsData(models.Model):
    aircraft_code = models.CharField(primary_key=True, max_length=3)
    model = models.TextField()  # This field type is a guess.
    range = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aircrafts_data'


class AirportsData(models.Model):
    airport_code = models.CharField(primary_key=True, max_length=3)
    airport_name = models.TextField()  # This field type is a guess.
    city = models.TextField()  # This field type is a guess.
    coordinates = models.TextField()  # This field type is a guess.
    timezone = models.TextField()

    class Meta:
        managed = False
        db_table = 'airports_data'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BoardingPasses(models.Model):
    ticket_no = models.ForeignKey('TicketFlights', models.DO_NOTHING, db_column='ticket_no', primary_key=True)
    flight_id = models.IntegerField()
    boarding_no = models.IntegerField()
    seat_no = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'boarding_passes'
        unique_together = (('flight_id', 'boarding_no'), ('flight_id', 'seat_no'), ('ticket_no', 'flight_id'),)


class Bookings(models.Model):
    book_ref = models.CharField(primary_key=True, max_length=6)
    book_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bookings'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Flights(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=6)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey(AirportsData, models.DO_NOTHING, db_column='departure_airport')
    arrival_airport = models.ForeignKey(AirportsData, models.DO_NOTHING, db_column='arrival_airport')
    status = models.CharField(max_length=20)
    aircraft_code = models.ForeignKey(AircraftsData, models.DO_NOTHING, db_column='aircraft_code')
    actual_departure = models.DateTimeField(blank=True, null=True)
    actual_arrival = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flights'
        unique_together = (('flight_no', 'scheduled_departure'),)


class Seats(models.Model):
    aircraft_code = models.ForeignKey(AircraftsData, models.DO_NOTHING, db_column='aircraft_code', primary_key=True)
    seat_no = models.CharField(max_length=4)
    fare_conditions = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'seats'
        unique_together = (('aircraft_code', 'seat_no'),)


class TicketFlights(models.Model):
    ticket_no = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='ticket_no', primary_key=True)
    flight = models.ForeignKey(Flights, models.DO_NOTHING)
    fare_conditions = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ticket_flights'
        unique_together = (('ticket_no', 'flight'),)


class Tickets(models.Model):
    ticket_no = models.CharField(primary_key=True, max_length=13)
    book_ref = models.ForeignKey(Bookings, models.DO_NOTHING, db_column='book_ref')
    passenger_id = models.CharField(max_length=20)
    passenger_name = models.TextField()
    contact_data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tickets'
