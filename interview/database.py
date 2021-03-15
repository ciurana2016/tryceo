import mysql.connector as mysql



class DatabaseConnection(object):

    CONFIG = {
    'user': 'candidate',
    'password': 'Fbps9Y7MhKQa4XPxjYo8',
    'host': '34.78.52.157',
    'database': 'Hiring_task',
    'raise_on_warnings': True
    }

    def __init__(self):
        self.connect()

    def connect(self):
        self.cnx = mysql.connect(**self.CONFIG)

    def disconnect(self):
        self.cnx.close()

    def test_query(self, query_string:str) -> int:
        # Just for test purposes
        self.cursor = self.cnx.cursor()
        self.cursor.execute(query_string)
        response = self.cursor.fetchone()[0]
        self.cursor.close()
        return response

    def query_hotel_data(self):
        # Query the hotel data we need to populate our own
        # database with the filtered results.
        self.cursor = self.cnx.cursor()

        self.cursor.close()

