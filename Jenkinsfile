pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.prod.local.yml'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/esinkirill/lmnad-jenkins'
            }
        }



        stage('Build and Deploy') {
            steps {
                script {
                    // Запуск docker-compose с использованием файла .env для сборки и запуска контейнеров
                    sh "docker-compose -f ${DOCKER_COMPOSE_FILE} up -d --build"
                }
            }
        }
    }

    post {
        success {
            echo 'Build and deployment succeeded!'
        }
        failure {
            echo 'Build or deployment failed!'
        }
    }
}
