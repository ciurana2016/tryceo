from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from interview.views import IndexView, load_reviews



urlpatterns = [
    url(r'^$', IndexView.as_view()),
    path('load_reviews/', load_reviews),
    path('admin/', admin.site.urls),
]
