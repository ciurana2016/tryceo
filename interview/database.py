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

    def query_hotels_data(self) -> list:
        # Query the hotel data we need to populate our own
        # database with the filtered results,
        # then returns the data in a list of dicts.
        self.cursor = self.cnx.cursor()

        query = (
        """
            SELECT country_area, hotel_id, hotel_name, hotel_address, hotel_url, vfm
            FROM hotel_info
        """
        )
        self.cursor.execute(query)
        data = []
        for (country_area, hotel_id, hotel_name, hotel_address,
            hotel_url, vfm
        ) in self.cursor:
            data.append({
                'country_area': country_area,
                'hotel_id': hotel_id,
                'hotel_name': hotel_name,
                'hotel_address': hotel_address,
                'hotel_url': hotel_url,
                'vfm': vfm
            })

        self.cursor.close()
        return data

    def query_reviews_data(self) -> list:
        # Query the hotel data we need to populate our own
        # database with the filtered results,
        # then returns the data in a list of dicts.
        self.cursor = self.cnx.cursor()

        query = (
        """
            SELECT hotel_id, review_date, review_title, positive_content,
                negative_content, review_score
            FROM hotel_reviews
            WHERE review_date >= '2018-01-01' AND review_date <= '2019-01-01'
        """
        )
        self.cursor.execute(query)
        data = []
        for (
            hotel_id, review_date, review_title, positive_content,
            negative_content, review_score
        ) in self.cursor:
            data.append({
                'hotel_id' : hotel_id,
                'review_date' : review_date,
                'review_title' : review_title,
                'positive_content' : positive_content,
                'negative_content' : negative_content,
                'review_score' : review_score
            })

        self.cursor.close()
        return data
