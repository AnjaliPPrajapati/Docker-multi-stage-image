# Stage 1: Python reader code image
FROM python:3.12-alpine as python_reader
Run mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

# Stage 2: Combined Rabbitmq image and python reader code image
FROM rabbitmq:3.13-management-alpine as rabbitmq
VOLUME /var/lib/rabbitmq
ENV RABBITMQ_DEFAULT_USER your_username
ENV RABBITMQ_DEFAULT_PASS your_password
# Erlang coockie will be needed mostly if you are trying to make a cluster otherwise you can skip
ENV RABBITMQ_ERLANG_COOKIE TCTyLe9gckZOHrdG3Usrogf4FcMNJLg4xh0EaQp/H0Ikn5qOxot6K0V7
WORKDIR /code
COPY --from=python_reader /usr /usr
COPY --from=python_reader /code/* .
ENTRYPOINT rabbitmq-server -detached && \
    python main.py