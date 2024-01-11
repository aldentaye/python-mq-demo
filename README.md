# python-mq-demo
 
# base image
`docker build -t flask-app:latest .`

# flask app & nginx
```
minikube start
minikube addons enable ingress
kubectl apply -f deployment.yaml
kubectl apply -f ingress.yaml
```
# rabbitmq
```
kubectl apply -f rabbitmq-deployment.yaml
kubectl port-forward service/rabbitmq 15672:15672
```
