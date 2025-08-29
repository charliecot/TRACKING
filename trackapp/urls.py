from django.urls import path
from .views import home, track,subscribe, Contact_view

urlpatterns = [
    path('',home,name='home'),
    path('tack/', track, name='track'),
    path('subscribe/',subscribe, name='subscribe' ),
    path('contact/',Contact_view, name='contact' ),
]

