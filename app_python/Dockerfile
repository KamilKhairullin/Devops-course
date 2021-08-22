# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir pdm==1.8.0 &&\
    pdm install
CMD ["pdm", "run", "python3", "main.py"]