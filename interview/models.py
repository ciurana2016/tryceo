from django.db import models



class CountryArea(models.Model):

    name = models.CharField(max_length=45)

    def __str__(self):
        return f'CountyArea - {self.name}'


class Hotel(models.Model):

    country_area = models.ForeignKey(CountryArea, on_delete=models.CASCADE, null=True)
    hotel_id = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=300, null=True)
    vfm = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    reviews = models.IntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return f'Hotel - {self.name}'


class HotelReview(models.Model):

    UUID = models.CharField(max_length=36, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    positive_content = models.TextField()
    negative_content = models.TextField()
    review_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Review for hotel {self.hotel.name}'
