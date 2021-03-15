from django.test import TestCase

from .database import DatabaseConnection



class DatabaseConnectionTest(TestCase):

    def test_database_connection(self):
        DC = DatabaseConnection()
        self.assertEqual(DC.cnx.user, 'candidate')
        DC.cnx.close()

    def test_query(self):
        DC = DatabaseConnection()
        count_hotel_id = DC.test_query('SELECT COUNT(hotel_id) FROM hotel_info')
        DC.cnx.close()
        self.assertEqual(count_hotel_id, 3965)
