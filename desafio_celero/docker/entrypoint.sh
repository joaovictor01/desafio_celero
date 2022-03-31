#!/bin/bash
set -e

database="$SQL_DATABASE"
host="$SQL_HOST"
cmd="$@"

until PGPASSWORD=$SQL_PASSWORD psql -h "$host" -d "$database" -U "$SQL_USER" -c '\q'; do
    echo "Postgres is unavailable - sleeping"
    sleep 1
done
echo "Postgres is up!"

if [ "$MODE" = "development" ]; then
    echo "Creating migrations..."
    python manage.py makemigrations --noinput
    echo "Created!"
    python manage.py migrate --noinput
    echo "Migrated!"

    echo "Generating translations..."
    python3 manage.py makemessages --all --no-obsolete
    echo "Translations generated"
fi

echo "Compiling translations..."
python3 manage.py compilemessages -v 0
echo "Translations compiled"

if [ "$MODE" = "development" ]; then
    echo "Loading fixtures..."
    python manage.py loaddata */fixtures/dev/*.json
    echo "Done!"
fi

if [ "$MODE" = "production" ]; then
    echo "Starting desafio_celero as `whoami`"
    exec gunicorn --bind :8000 --limit-request-line 8190 --workers 5 --timeout $GUNICORN_TIMEOUT \
         desafio_celero.wsgi:application

elif [ "$MODE" = "development" ]; then
    echo "Starting desafio_celero as `whoami`"
    python manage.py runserver 0.0.0.0:8000
fi
