from django.test import TestCase
from .models import Menu, Booking

# Create the test class

class MenuTest(TestCase):
      
    def test_menu_item(self):
        menu_item = Menu.objects.create(title="Hotsilog", price=25, inventory=100)
        
        self.assertEqual(str(menu_item), 'Hotsilog : 25')

class BookingTest(TestCase):

    def test_booking(self):
        booking_item = Booking.objects.create(name="Oshi", no_of_guests=20, booking_date='2023-09-06')

        self.assertEqual(str(booking_item), 'Oshi : 20')

    def test_reservation_date(self):
        booking_item = Booking.objects.create(name="Jade", no_of_guests=10, booking_date='2023-09-20')

        self.assertGreaterEqual(booking_item.booking_date, '1999-01-21')


