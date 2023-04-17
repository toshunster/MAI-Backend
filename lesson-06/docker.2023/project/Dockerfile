FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r /app/requirements.txt


CMD ["python", "manage.py", "runserver"]
