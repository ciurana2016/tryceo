import mysql.connector as mysql

from .models import CountryArea, Hotel, HotelReview



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
                negative_content, review_score, UUID
            FROM hotel_reviews
            WHERE review_date >= '2018-01-01' AND review_date <= '2019-01-01'
        """
        )
        self.cursor.execute(query)
        data = []
        for (
            hotel_id, review_date, review_title, positive_content,
            negative_content, review_score, UUID
        ) in self.cursor:
            data.append({
                'UUID': UUID,
                'hotel_id' : hotel_id,
                'review_date' : review_date,
                'review_title' : review_title,
                'positive_content' : positive_content,
                'negative_content' : negative_content,
                'review_score' : review_score
            })

        self.cursor.close()
        return data


def filter_and_save_data():
    """
        1. Query the database with DatabaseConnection.
        2. Save data into our models (country_areas, hotels, reviews).
    """
    Database = DatabaseConnection()
    hotels = Database.query_hotels_data()
    reviews = Database.query_reviews_data()


    # [1] Create hotels
    for hotel in hotels:

        # Create the region if we don't have it
        # if not CountryArea.objects.filter(name=hotel['country_area']).exists():
        country_area = CountryArea.objects.create(name=hotel['country_area'])
        # else:
        #     country_area = CountryArea.objects.get(name=hotel['country_area'])

        # Create the hotel if we don't have it
        # if not Hotel.objects.filter(name=['hotel_name']).exists():
        Hotel.objects.create(
            country_area = country_area,
            hotel_id = hotel['hotel_id'],
            name = hotel['hotel_name'],
            address = hotel['hotel_address'],
            url = hotel['hotel_url'],
            vfm = hotel['vfm']
        )


    assert len(hotels) == Hotel.objects.all().count()


    # [2] Create reviews if we don't have them
    for review in reviews:
        # if not HotelReview.objects.filter(UUID=review['UUID']).exists():
        hotel = Hotel.objects.get(hotel_id=review['hotel_id'])
        HotelReview.objects.create(
            UUID = review['UUID'],
            hotel = hotel,
            date = review['review_date'],
            title = review['review_title'],
            positive_content = review['positive_content'],
            negative_content = review['negative_content'],
            review_score = review['review_score'],
        )
        # Simple cont of the reviews
        hotel.reviews += 1
        hotel.save()


    assert len(reviews) == HotelReview.objects.all().count()

    # [3] Remove hotels (with reviews) if less than 5 reviews
    Hotel.objects.filter(reviews__lt=5).delete()
