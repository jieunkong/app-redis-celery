docker build -t celery-study-app .

echo 

docker-compose down
docker-compose up -d 

echo

docker ps | grep celery-study

echo 