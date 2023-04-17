FROM python:3.6

RUN mkdir /app
ADD . /app

WORKDIR /app
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:8000"]
