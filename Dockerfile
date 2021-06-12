FROM python:3.9.2

WORKDIR /fastai

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]