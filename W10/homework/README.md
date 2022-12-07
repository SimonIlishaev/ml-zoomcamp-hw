# Necessary commands

* create local cluster

```zsh
kind create cluster
```

* upload docker image to the cluster

```zsh
kind load docker-image <name>:<tag>
```

* create deployment

```zsh
kubectl apply -f deployment.yaml
```

* create service

```zsh
kubectl apply -f service.yaml
```

* port forward

```zsh
kubectl port-forward service/credit-card 9696:80
```

* test service

```zsh
python q6_test.py
```

* Autoscaling

```zsh
kubectl autoscale deployment credit-card --name credit-card-hpa --cpu-percent=20 --min=1 --max=3
```

* Check created HPA

```zsh
kubectl get hpa
```
