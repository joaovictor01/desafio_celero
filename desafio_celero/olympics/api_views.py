"""App API views."""
from rest_framework import viewsets, filters
from olympics.models import Athlete, Event, Game, Medal
from olympics.serializers import AthleteSerializer, EventSerializer, GameSerializer, MedalSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    """Athlete API ViewSet"""
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Event API ViewSet"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GameViewSet(viewsets.ModelViewSet):
    """Event API ViewSet"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class MedalViewSet(viewsets.ModelViewSet):
    """Event API ViewSet"""
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
