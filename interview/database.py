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
