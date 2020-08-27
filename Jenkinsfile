pipeline {
    agent any

    stages {
        stage('Create S3 Bucket') {
            steps {
                sh 'python s3Bucket.py'
            }
        }
        stage('Create Cluster on AWS') {
            steps {
                sh 'python clusterCreation.py'
            }
        }
        stage('Cluster Validation') {
            steps {
                sh 'python clusterValidation.py'
            }
        }
        stage('Nginx Deployment & LoadBalancer') {
            steps {
                sh 'python nginxDeployment.py'
            }
        }
    }
}
