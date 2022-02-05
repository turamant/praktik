#!/bin/bash
# pipenv shell
case $1 in
  desk)
    docker-compose -f docker-compose.prod.desk.yml down -v
    docker-compose -f docker-compose.prod.desk.yml up -d --build
    docker-compose -f docker-compose.prod.desk.yml exec web python manage.py makemigrations --noinput
    docker-compose -f docker-compose.prod.desk.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.desk.yml exec web python manage.py createsuperuser
    docker-compose -f docker-compose.prod.desk.yml exec web python manage.py collectstatic --no-input --clear
    echo 'откройте 127.0.0.1:1337 в браузере'
    echo 'остановить контейнеры -= sh prod.sh stop =-'
    ;;

  server)
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
    echo 'откройте ip сервера в браузере'
    echo 'остановить контейнеры -= sh prod.sh stop =-'
    ;;

  stop)
    docker-compose -f docker-compose.prod.yml down -v
    ;;
esac