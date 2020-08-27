import os

# Validating cluster setup.
os.system('kops validate cluster --state=s3://starkware-state --name=myfirstcluster.k8s.local --wait 10m')