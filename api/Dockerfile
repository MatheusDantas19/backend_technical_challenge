FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . .
RUN pip install -r requirements.txt

RUN python manage.py makemigrations

EXPOSE 8000