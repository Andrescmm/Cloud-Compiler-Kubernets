## Deploy cloud compiler

bash
docker build -t cloud-compiler-parcial .
docker run -p 8080:8080 cloud-compiler-parcial


For Kubernets 

Luego, etiqueta la imagen Docker con un nombre más descriptivo:

bash
docker tag cloud-compiler-parcial andrescmm/cloud-compiler-parcial

Inicia sesión


 en Docker (si aún no lo has hecho) y sube la imagen Docker al registro de Docker:

bash
docker login
docker push andrescmm/cloud-compiler-parcial

A continuación, aplica los archivos YAML de despliegue y servicio para el backend en Kubernetes:
bash
kubectl apply -f deployment.yml
kubectl get deployments
kubectl get services

Utiliza el siguiente comando para obtener información sobre los servicios y los puertos asignados:

bash
kubectl get services --all-namespaces

