"""Athletes serializers."""
from rest_framework import serializers
from olympics.models import Athlete, Event, Game, Medal


class AthleteSerializer(serializers.ModelSerializer):
    """
    Athlete Model Serializer.
    """
    class Meta:
        model = Athlete
        fields = '__all__'
        datatables_always_serialize = ('id',)
        depth = 2


class EventSerializer(serializers.ModelSerializer):
    """
    Event Model Serializer.
    """
    class Meta:
        model = Event
        fields = '__all__'
        datatables_always_serialize = ('id',)
        depth = 1


class GameSerializer(serializers.ModelSerializer):
    """
    Event Model Serializer.
    """
    class Meta:
        model = Game
        fields = '__all__'
        datatables_always_serialize = ('id',)
        depth = 1


class MedalSerializer(serializers.ModelSerializer):
    """
    Event Model Serializer.
    """
    class Meta:
        model = Medal
        fields = '__all__'
        datatables_always_serialize = ('id',)
        depth = 2


class CSVFileUploadSerializer(serializers.Serializer):
    """
    CsvUpload Serializer
    """
    csv_file = serializers.FileField()

    class Meta:
        fields = ('csv_file', )
