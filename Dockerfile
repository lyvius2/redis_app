FROM python:3.11.1

COPY app / app/

WORKDIR /app

RUN pip install redis redlock-py redis-om

CMD ["sleep", "infinity"]
