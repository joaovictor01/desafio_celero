"""Django settings loader."""
import os

from django.core.management.utils import get_random_secret_key


if os.getenv('MODE') == 'production':
    from desafio_celero.settings.production import *
else:
    from desafio_celero.settings.development import *

# Secret Key Configuration
if os.path.exists(os.path.join(BASE_DIR, 'secret_key.txt')):  # NOQA
    with open(os.path.join(BASE_DIR, 'secret_key.txt'), 'r') as file:  # NOQA
        SECRET_KEY = file.read().strip()
else:
    SECRET_KEY = get_random_secret_key()
    with open(os.path.join(BASE_DIR, 'secret_key.txt'), 'w', encoding='UTF-8') as file:  # NOQA
        file.write(SECRET_KEY)
