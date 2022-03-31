"""App models."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Event(models.Model):
    """Event model."""
    name = models.CharField(verbose_name=_('Event'), max_length=256)
    sport = models.CharField(verbose_name=_('Sport'), max_length=256)

    class Meta:
        """Event Meta."""
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ['name', ]

    def __str__(self):
        """To string model display. """
        return self.name


class Game(models.Model):
    """Game model"""
    class Season(models.TextChoices):
        """Season model."""
        SUMMER = 'Summer', _('Summer')
        WINTER = 'Winter', _('Winter')

    name = models.CharField(verbose_name=_('Game name'), max_length=128)
    year = models.IntegerField(verbose_name=_('Year'))
    season = models.CharField(verbose_name=_('Season'), choices=Season.choices, max_length=64)
    city = models.CharField(verbose_name=_('City'), max_length=256)
    events = models.ManyToManyField(Event, related_name='games', verbose_name=_('Events'), blank=True)

    class Meta:
        """Game meta."""
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
        ordering = ['year', ]

    def __str__(self):
        """To string model display. """
        return self.name


class Athlete(models.Model):
    """Athlete model."""
    class Sex(models.TextChoices):
        """Sex Model."""
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    id = models.IntegerField(verbose_name=_('ID'), primary_key=True)
    name = models.CharField(verbose_name=_('Name'), max_length=128)
    sex = models.CharField(verbose_name=_('Sex'), choices=Sex.choices, max_length=1)
    age = models.IntegerField(verbose_name=_('Age'), blank=True, null=True)
    height = models.DecimalField(verbose_name=_('Height'), max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(verbose_name=_('Weight'), max_digits=5, decimal_places=2, blank=True, null=True)
    team = models.CharField(verbose_name=_('Team/Country'), max_length=128)
    noc = models.CharField(verbose_name=_('National Olympic Committee'), max_length=3)

    class Meta:
        """Athlete Meta."""
        verbose_name = _('Athlete')
        verbose_name_plural = _('Athletes')
        ordering = ['id', ]

    def __str__(self):
        """To string model display. """
        return self.name


class Medal(models.Model):
    class MedalName(models.TextChoices):
        """Medal model."""
        GOLD = 'Gold', _('Gold')
        SILVER = 'Silver', _('Silver')
        BRONZE = 'Bronze', _('Bronze')
        NA = 'NA', _('No medal')

    medal = models.CharField(verbose_name=_('Medal'), choices=MedalName.choices, max_length=16, blank=True, null=True)
    athlete = models.ForeignKey('olympics.Athlete', verbose_name=_('Athlete'), on_delete=models.CASCADE)
    event = models.ForeignKey('olympics.Event', verbose_name=_('Event'), on_delete=models.CASCADE)
    game = models.ForeignKey('olympics.Game', verbose_name=_('Game'), on_delete=models.CASCADE)

    class Meta:
        """Medal meta"""
        verbose_name = _('Medal')
        verbose_name_plural = _('Medals')
        ordering = ['game__year']

