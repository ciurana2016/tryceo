from interview.models import CountryArea
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Load the country areas for the table.
        context['country_areas'] = CountryArea.objects.all().order_by('name')

        return context
