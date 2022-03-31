"""Olympics tasks."""
import traceback
import logging
from olympics.models import Athlete, Event, Game, Medal
from desafio_celero.celery import APP
from olympics.utils import csv_to_json

logger = logging.getLogger('celery')


@APP.task
def parse_json_content(csv_file):
    json_content = csv_to_json(csv_file)
    try:
        for element in json_content:
            athlete, created = Athlete.objects.get_or_create(
                id=int(element.get('ID')),
                defaults={
                    'name': element.get('Name'),
                    'sex': element.get('Sex'),
                    'age': element.get('Age') if element.get('Age') != 'NA' else None,
                    'height': element.get('Height') if element.get('Height') != 'NA' else None,
                    'weight': element.get('Weight') if element.get('Weight') != 'NA' else None,
                    'team': element.get('Team'),
                    'noc': element.get('NOC'),
                }
            )

            event, created = Event.objects.get_or_create(
                name=element.get('Event'),
                defaults={'sport': element.get('Sport')}
            )

            game, created = Game.objects.get_or_create(
                name=element.get('Games'),
                defaults={
                    'year': element.get('Year'),
                    'season': element.get('Season'),
                    'city': element.get('City')
                }
            )
            game.events.add(event)

            medal, created = Medal.objects.get_or_create(
                athlete=athlete,
                event=event,
                game=game,
                defaults={'medal': str(element.get('Medal'))}
            )
            logger.debug('Row: %s added!', element)
    except FileNotFoundError:
        logger.error('CSV file not found!')
    except Exception as error:
        logger.error('Error parsing CSV file! %s', error)
        logger.debug(traceback.format_exc())
