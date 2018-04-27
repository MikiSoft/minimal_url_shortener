from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'shorten/', views.shorten),
    url(r'(?P<slug>([A-z]|\d){8})', views.open, name="open"),
]