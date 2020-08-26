import os
import boto3

# Creating S3 Bucket
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='foo21312')

# Creating K8S cluster on AWS, it will take 5-10 minutes.
os.system('kops create cluster \
--name myfirstcluster.k8s.local \
--zones us-east-1a,us-east-1b,us-east-1c \
--state s3://starkware-state \
--node-count=3 \
--master-count=3 \
--yes')

# Validating cluster setup.
os.system('kops validate cluster --state=s3://starkware-state --name=myfirstcluster.k8s.local --wait 10m')

# Deploying a NGINX server & LoadBalancer
os.system('kubectl create -f nginx_deployment.yaml')
os.system('kubectl create -f nginx_service.yaml')







