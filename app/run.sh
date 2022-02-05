#!/bin/bash
# pipenv shell
case $1 in
  dev)

    docker-compose down -v
    docker-compose up -d --build
    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py createsuperuser
    echo '127.0.0.1:8000 откройте в браузере'
    ;;
  prod)
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
    echo '127.0.0.1:8000 откройте в браузере'
    ;;
esac