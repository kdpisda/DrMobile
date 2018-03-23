from django.conf.urls import url
from .views import register ,index,registration

urlpatterns = [
    url(r'^$', index , name="index"),
    url(r'^registration/',registration),
    url(r'^register/', register , name="register"),
]