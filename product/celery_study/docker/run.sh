#!/bin/sh
docker-compose down
docker-compose up -d

echo

docker-compose logs -f

echo