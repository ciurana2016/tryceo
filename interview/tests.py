from unittest import skip
from django.test import TestCase
from django.utils import timezone

from .database import DatabaseConnection, filter_and_save_data
from .models import CountryArea, Hotel, HotelReview



class CountryAreaModelTest(TestCase):

    def test_country_area_model(self):
        test_name = 'test_area'
        CountryArea.objects.create(name=test_name)
        test_area = CountryArea.objects.first()
        self.assertEqual(test_area.name, test_name)


class HotelModelTest(TestCase):

    def setUp(self):
        self.test_area = CountryArea.objects.create(name='test_area')

    def test_hotel_model(self):
        test_name = 'test_hotel'
        Hotel.objects.create(
            country_area = self.test_area,
            hotel_id = 'test_id',
            name = test_name,
            address = 'test_address',
            url = 'https://test.com',
            vfm = 234.65
        )
        test_hotel = Hotel.objects.first()
        self.assertEqual(test_hotel.name, test_name)
        self.assertEqual(test_hotel.country_area, self.test_area)


class HotelReviewModelTest(TestCase):

    def setUp(self):
        self.test_area = CountryArea.objects.create(name='test_area')
        self.hotel = Hotel.objects.create(
            country_area = self.test_area,
            hotel_id = 'test_id',
            name = 'test_hotel_name',
            address = 'test_address',
            url = 'https://test.com',
            vfm = 234.65
        )

    def test_hotel_review_model(self):
        positive_content = 'Lorem ipsum dolor'
        HotelReview.objects.create(
            UUID = 'h490bg',
            hotel = self.hotel,
            date = timezone.now(),
            title = 'test_title',
            positive_content = positive_content,
            negative_content = 'negative_test',
            review_score = 234.56
        )
        test_review = HotelReview.objects.first()
        self.assertEqual(test_review.positive_content, positive_content)
        self.assertEqual(test_review.hotel, self.hotel)

    def test_hotel_deletion_deletes_review(self):
        test_review = HotelReview.objects.create(
            hotel = self.hotel,
            date = timezone.now(),
            title = 'test_title',
            positive_content = 'positive_test',
            negative_content = 'negative_test',
            review_score = 234.56
        )
        Hotel.objects.first().delete()
        self.assertEqual(HotelReview.objects.all().count(), 0)


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

    def test_query_hotels_data(self):
        DC = DatabaseConnection()
        data = DC.query_hotels_data()
        self.assertEqual(len(data), 3965)
        DC.cnx.close()

    @skip('Query takes 10 seconds')
    def test_query_reviews_data(self):
        DC = DatabaseConnection()
        data = DC.query_reviews_data()
        self.assertEqual(len(data), 376603)
        DC.cnx.close()


class FilterAndSaveDataTest(TestCase):

    def test_function(self):
        self.assertEqual(Hotel.objects.all().count(), 0)
        filter_and_save_data()
        self.assertTrue(Hotel.objects.all().count() > 1)
        # self.assertEqual(Hotel.objects.filter(reviews__lt=5).count(), 0)
