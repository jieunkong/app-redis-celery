# app-redis-celery

## 요구사항
docker 컨테이너를 app, message queue, core로 3개로 만들어서 </br>
app 에서 메시지를 만들어서 queue로 던지고 </br>
core에서 해당 메시지를 받아서 응답 메시지를 만든 후 </br>
app에서 리턴 받은 메시지를 출력하는 샘플 구조 구현하기 </br>

## docker container
1. app
    - api server
2. redis
    - message queue
3. core
    - celery worker

## 프로젝트 실행방법
1. Clone this repository.
2. Run project. <br>
    `cd app-redis-celery/product/celery_study/docker` <br>
    `./run.sh`

## 프로젝트 구조
    .
    ├── README.md
    ├── common
    │   ├── const
    │   ├── db
    │   ├── depends
    │   ├── mappers
    │   ├── middleware
    │   ├── models
    │   ├── schemas
    │   ├── services
    │   ├── tests
    │   └── utils
    │       └── singleton.py
    ├── data
    │   ├── files
    │   └── logs
    └── product
        └── celery_study
            ├── app
            │   ├── __init__.py
            │   ├── main.py
            │   ├── routers
            │   │   ├── __init__.py
            │   │   └── v1
            │   │       ├── __init__.py
            │   │       └── user_route.py
            │   ├── run_celery.py
            │   └── tests
            │       ├── __init__.py
            │       └── test_user.py
            ├── common
            ├── config
            │   └── app_config.py
            ├── core
            │   ├── run_celery.py
            │   └── tasks
            │       └── user_task.py
            └── docker
                ├── Dockerfile
                ├── docker-compose.yml
                ├── requirements.txt
                └── run.sh