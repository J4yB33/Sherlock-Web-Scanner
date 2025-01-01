ARG PYTHON_VERSION=3.9-alpine
FROM python:${PYTHON_VERSION} AS base

ARG USER_NAME=swebscan
ARG UID=1000
ARG GID=1000

RUN python3 -m pip install --no-cache-dir --upgrade pip

COPY requirements.txt /opt/requirements.txt
RUN python3 -m pip install -r /opt/requirements.txt

RUN addgroup -S $USER_NAME -g $GID; adduser -S $USER_NAME -u $UID -G $USER_NAME
ENV USER $USER_NAME

WORKDIR /app
EXPOSE 5001

COPY . .
RUN chown -R $USER_NAME:$USER_NAME /app

USER $USER_NAME

ENTRYPOINT ["python3", "/app/sherlock_app.py"]
