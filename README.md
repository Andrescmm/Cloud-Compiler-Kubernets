## Deploy cloud compiler

```bash
docker build -t cloud-compiler-parcial .
docker run -p 8080:8080 cloud-compiler-parcial
```

For Kubernets 



```bash
docker tag cloud-compiler-parcial andrescmm/cloud-compiler-parcial
```
Inicia sesión

```bash
docker login
docker push andrescmm/cloud-compiler-parcial
```

```bash
kubectl apply -f deployment.yml
kubectl scale deployment cloud-compiler-parcial --replicas=1
kubectl get deployments
kubectl get services

kubectl get pods --all-namespaces
kubectl delete deployment --namespace=default --all
kubectl scale deployment cloud-compiler-parcial --replicas=0
```
```bash
kubectl get services --all-namespaces

```
