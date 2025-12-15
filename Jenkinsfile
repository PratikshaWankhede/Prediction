pipeline {
    agent any

    environment {
        IMAGE_NAME = "pratikshawankhede/churnprediction_app"
        TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-creds', variable: 'DOCKER_PASS')]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u pratikshawankhede --password-stdin
                      docker push $IMAGE_NAME:$TAG
                      docker logout
                    '''
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                  docker-compose down || true
                  docker-compose pull
                  docker-compose up -d
                '''
            }
        }
    }
}

