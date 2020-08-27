import os

# Creating K8S cluster on AWS with 3 masters and 3 workers, it will take 5-10 minutes.
os.system('kops create cluster \
--name myfirstcluster.k8s.local \
--zones us-east-1a,us-east-1b,us-east-1c \
--state s3://starkware-state \
--node-count=3 \
--master-count=3 \
--yes')