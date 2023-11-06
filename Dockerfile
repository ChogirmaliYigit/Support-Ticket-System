FROM python:3.11.4
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y gettext jq
RUN pip install -r requirements.txt
COPY . /code/
