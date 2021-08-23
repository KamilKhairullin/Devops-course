# syntax=docker/dockerfile:1

FROM python:3.8-alpine
RUN apk add build-base 
WORKDIR /app
<<<<<<< HEAD

RUN adduser -D app && chown -R app /app
RUN mkdir /myapp-tmp-dir && chown -R app /myapp-tmp-dir

COPY myapp/pyproject.toml .
COPY myapp/pdm.lock .
RUN pip3 install --no-cache-dir pdm==1.8.0 &&\ 
    pdm install

EXPOSE 5000

COPY /myapp .
CMD pdm run python3 main.py
=======
COPY pyproject.toml .
COPY pdm.lock .
RUN pip3 install --no-cache-dir pdm==1.8.0 &&\
    pdm install
COPY . .
CMD ["pdm", "run", "python3", "main.py"]
>>>>>>> f10645d22061e9810af27128451ab1a038df58dc
