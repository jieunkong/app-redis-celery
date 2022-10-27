FROM python:3.10

COPY requirements.txt /install/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /install/requirements.txt

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_PORT
EXPOSE ${APP_PORT}

ARG BUILD_VER
ENV BUILD_VER=${BUILD_VER}