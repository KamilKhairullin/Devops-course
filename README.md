<h3 align="center">
    DevOps course at Innopolis University. Kamil Khairullin.
<h3>


# Quick start

## Overview 
 Web application written in Flask and showing the current Moscow time.
 Visit to access current time
 ```
 localhost:5000/
 ```
Visit to show all visitors and time of their visit.
```
localhost:5000/visits
```
## Install
1. Clone directory
```
git clone https://github.com/KamilKhairullin/devops.git
```
2. Go to app folder
```
cd app_python
cd myapp
```
3. Run
```
pip3 install pdm==1.8.0
```
4. In app_python folder run 
```
pdm install
```
## Run using minikube and kubectl
1. Install minikube and kubectl
```
brew install kubectl
```
```
brew install minikube
```

2. Run 
```
minikube start
```

3. Run 
```
minikube dashboard
```

to access web interface of minikube

4. Create deployment of your docker image
```
kubectl create deployment myapp --image=kamilkhairullin/devops_inno:latest
```

5. Expose deployment
```
kubectl expose deployment myapp --type=LoadBalancer --port=5000
```

6. Run to access application
```
minikube service myapp
```

## Install using .yml file
1. Create deployment.yml and service.yml (see example in repo)

2. Run
```
kubectl apply -f deployment.yml
```
```
kubectl apply -f service.yml
```
3. Run 
```
minikube service myapp-service
```

## HELM

1. Create chart
```
helm create my-app 
```

2. Install app
```
helm package my-app
```
```
helm install my-app ./my-app-0.1.0.tgz
```
```
minikube service my-app
```
    
## Run using Docker
### Build locally
Run in /app_python folder
```
docker build -t devops_inno .
```
### Run using local build
```
docker run -p 5000:5000 devops_inno
```
### Download image from DockerHub
```
docker pull kamilkhairullin/devops_inno:latest
```
### Run 
```
docker run -p 5000:5000 kamilkhairullin/devops_inno:latest
```
    
## Run using python 
After installation, run the app
```
pdm run python3 main.py
```
and access it in browser
```
localhost:5000
```

## Unit testing
To run unit tests go to tests folder and run
```
pdm run pytest
```
