pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "pratikshawankhede/churnprediction_app"
        DOCKERHUB_CREDENTIALS = "dockerhub-creds"
        DEPLOY_DIR = "/home/ubuntu/ChurnPrediction"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                  docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .
                  docker tag $DOCKER_IMAGE:$BUILD_NUMBER $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKERHUB_CREDENTIALS,
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push $DOCKER_IMAGE:$BUILD_NUMBER
                      docker push $DOCKER_IMAGE:latest
                      docker logout || true
                    '''
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                dir(DEPLOY_DIR) {
                    sh '''
                      docker-compose pull app || docker compose pull app
                      docker-compose down app || docker compose down
                      docker-compose up -d app || docker compose up -d app
                    '''
                }
            }
        }
    }
}

