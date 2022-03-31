"""App API views."""
import os
from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from olympics.models import Athlete, Event, Game, Medal
from olympics.serializers import AthleteSerializer, EventSerializer, GameSerializer, MedalSerializer,\
    CSVFileUploadSerializer
from olympics.tasks import csv_to_json, parse_json_content
from django.core.files.storage import FileSystemStorage


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


class CSVFileUploadAPIView(CreateAPIView):
    serializer_class = CSVFileUploadSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']
        fs = FileSystemStorage(csv_file.temporary_file_path())
        parse_json_content.delay(fs.location)
        return Response(status=204)
