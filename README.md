<h3 align="center">
    DevOps Lab 1 & 2. Kamil Khairullin.
<h3>



# Quick start

## Overview 
 Web application written in Flask and showing the current time in Moscow
## Install
1. Clone directory
```
git clone https://github.com/KamilKhairullin/devops.git
```
2. Go to app folder
```
cd app_python
```
3. Run
```
pip3 install pdm==1.0.4
```
4. In app_python folder run 
```
pdm install
```

## Run
After installation, run the app
```
pdm run python3 main.py
```
and access it in browser
```
localhost:5000
```
## Docker
### Build locally
Run in /app_python folder
```
docker build -t kamilkhairullin/devops_inno .
```
### Download image from DockerHub
```
docker pull kamilkhairullin/devops_inno:latest
```
### Run 
```
docker run -p 5000:5000 kamilkhairullin/devops_inno:latest
```
