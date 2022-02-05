#!/bin/bash
# pipenv shell
case $1 in
  run)

    docker-compose down -v
    docker-compose up -d --build
    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py createsuperuser
    echo '127.0.0.1:8000 откройте в браузере'
    echo 'остановить контейнеры -= sh dev.sh stop =-'
    ;;
  stop)
    docker-compose down -v
    ;;
esac