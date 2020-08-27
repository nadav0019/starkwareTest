import os

# Deploying a NGINX server & LoadBalancer (Nginx-elb service)
os.system('kubectl create -f nginx_deployment.yaml')
os.system('kubectl create -f nginx_service.yaml')







