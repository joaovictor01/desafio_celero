""" desafio_celero API Urls."""
from rest_framework import routers
from django.urls import path, include
from olympics.api_views import AthleteViewSet, EventViewSet
from olympics.api_views import CSVFileUploadAPIView


router = routers.DefaultRouter()
router.register(r'athletes', AthleteViewSet, basename='athletes')
router.register(r'events', EventViewSet, basename='events')
router.register(r'games', EventViewSet, basename='games')
router.register(r'medals', EventViewSet, basename='medals')


app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('upload/', CSVFileUploadAPIView.as_view())
]
