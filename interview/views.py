from django.http.response import JsonResponse
import json

from interview.models import CountryArea, HotelReview
from django.views.generic import TemplateView
from django.http import JsonResponse

from app.settings import MAPBOX_KEY



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Mapbox api key
        context['MAPBOX_KEY'] = MAPBOX_KEY

        # Load the country areas for the table.
        context['country_areas'] = CountryArea.objects.all().order_by('name')

        return context


def load_reviews(request) -> JsonResponse:
    data = json.loads(request.body.decode('utf-8'))

    if 'all' in data.keys():
        print('ALL REVIEWS')
    else:
        print('SOME REVIEWS')

    return JsonResponse({'ok': True})
