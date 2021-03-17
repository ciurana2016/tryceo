from interview.models import CountryArea, Hotel
from django.views.generic import TemplateView

from app.settings import MAPBOX_KEY



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Mapbox api key
        context['MAPBOX_KEY'] = MAPBOX_KEY

        # Load the country areas for the table.
        context['country_areas'] = CountryArea.objects.all().order_by('name')

        # TODO -- from here down make tests
        # Load the hotels,
        context['hotels'] = Hotel.objects.all()[:10]

        return context
