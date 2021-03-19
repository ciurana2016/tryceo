import json

from interview.models import CountryArea, HotelReview
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers

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
    n_results = 100
    response_data = {
        'reviews': None,
    }

    # Query all or selected regions reviews
    if 'all' in data.keys():
        reviews = HotelReview.objects.all().order_by('-review_score', '-date')
    else:
        print('SOME REVIEWS')
        reviews = False

    # Make the paginator for the results
    paginator = Paginator(reviews, n_results)
    current_page = paginator.page(1)
    response_data['reviews'] = serializers.serialize(
        'json',
        current_page,
        use_natural_foreign_keys=True,
        use_natural_primary_keys=True
    )
    if current_page.has_next():
        response_data['next_page_number'] = current_page.next_page_number()
    if current_page.has_previous():
        response_data['prev_page_number'] = current_page.previous_page_number()

    return JsonResponse(response_data)
