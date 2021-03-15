from django.test import TestCase

from .database import DatabaseConnection



class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        DC = DatabaseConnection()
        self.assertEqual(DC.cnx.user, 'candidate')
        DC.cnx.close()
