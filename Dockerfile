FROM python:3.9.2

WORKDIR /fastai

ENV PYTHONUNBUFFERED True
ENV PORT=8080


COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app