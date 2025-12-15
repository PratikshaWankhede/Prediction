pipeline {
    agent any

    environment {
        IMAGE_NAME = "pratikshawankhede/churnprediction_app"
        IMAGE_TAG  = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                  docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push ${IMAGE_NAME}:${IMAGE_TAG}
                      docker logout
                    """
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh """
                  docker-compose down || true
                  docker-compose pull
                  docker-compose up -d
                """
            }
        }
    }
}

