FROM python:3.13.2-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD [ "python3", "app.py"]