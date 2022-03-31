from django.contrib import admin
from olympics.models import Athlete, Event, Game, Medal


class AthleteAdmin(admin.ModelAdmin):
    """
    AthleteAdmin is an administrator view for the :model:`athlete.models.Athlete`.
    """
    list_display = ('name', 'sex', 'age', 'height', 'weight', 'team', 'noc')


class EventAdmin(admin.ModelAdmin):
    """
    EventAdmin is an administrator view for the :model:`event.models.Event`.
    """
    list_display = ('name', 'sport')


class GameAdmin(admin.ModelAdmin):
    """
    GameAdmin is an administrator view for the :model:`event.models.Event`.
    """
    list_display = ('name', 'year', 'season', 'city')


class MedalAdmin(admin.ModelAdmin):
    """
    MedalAdmin is an administrator view for the :model:`event.models.Event`.
    """
    list_display = ('medal', 'athlete', 'event', 'game')


admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Medal, MedalAdmin)
