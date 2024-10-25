FROM python:3.13

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install -r requirements.txt

COPY . .

RUN python -m pip install .
