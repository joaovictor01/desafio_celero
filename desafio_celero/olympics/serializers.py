"""Athletes serializers."""
from rest_framework import serializers, filters
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
    events = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=True)

    class Meta:
        model = Game
        fields = '__all__'
        datatables_always_serialize = ('id',)
        lookup_field = 'events'
        depth = 2


class MedalSerializer(serializers.ModelSerializer):
    """
    Event Model Serializer.
    """
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

    class Meta:
        model = Medal
        fields = ('medal', 'athlete', 'event', 'game')
        datatables_always_serialize = ('id', )
        lookup_field = ('athlete', 'event', 'game')
        depth = 3


class CSVFileUploadSerializer(serializers.Serializer):
    """
    CsvUpload Serializer
    """
    csv_file = serializers.FileField()

    class Meta:
        fields = ('csv_file', )
