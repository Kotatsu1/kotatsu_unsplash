FROM python:3.10.11-slim-buster

COPY . .

RUN pip install -r requirements.txt

CMD 'python' 'src/main.py'