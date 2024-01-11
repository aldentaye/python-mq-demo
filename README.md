# python-mq-demo

# login to ghcr
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic
`echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin`

# manually pull to inspect image
`docker pull ghcr.io/aldentaye/python-mq-demo:main`

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
