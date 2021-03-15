from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from interview.views import IndexView



urlpatterns = [
    url(r'^$', IndexView.as_view()),
    path('admin/', admin.site.urls),
]
