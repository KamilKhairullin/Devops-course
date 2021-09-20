# Lab 9

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