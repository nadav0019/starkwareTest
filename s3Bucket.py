import boto3

# Creating S3 Bucket
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='starkware-state')