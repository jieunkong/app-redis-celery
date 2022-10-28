#!/bin/sh

docker build -t celery-study-app .

echo 

docker-compose down
docker-compose up -d 

echo

docker-compose logs -f 

echo 