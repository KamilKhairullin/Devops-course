# syntax=docker/dockerfile:1

FROM python:3.8-alpine
RUN apk add build-base 
WORKDIR /app

RUN adduser -D app sudo && chown -R app /app
RUN mkdir /myapp-tmp-dir && chown -R app /myapp-tmp-dir

USER app 

COPY myapp/pyproject.toml .
COPY myapp/pdm.lock .
RUN pip3 install --no-cache-dir pdm==1.8.0 &&\ 
    python -m pdm install

EXPOSE 5000
COPY /myapp .
CMD ["python", "-m", "pdm", "run", "python3", "main.py"]
