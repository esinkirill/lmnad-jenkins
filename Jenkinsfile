pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.prod.local.yml'
        ENV_FILE_PATH = '/home/esinkirill/lmnad_prod_work/.env' // путь к файлу .env на хосте
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Клонируем репозиторий
                git 'https://github.com/esinkirill/lmnad-jenkins'
            }
        }

    stage('Copy .env file') {
        steps {
            // Копируем файл .env с хоста внутрь контейнера Jenkins
            sh "cp ${ENV_FILE_PATH} /var/jenkins_home/workspace/lmnad-jenkins/.env"
        }
    }



        stage('Build and Deploy') {
            steps {
                script {
                    // Запуск docker-compose с использованием файла .env для сборки и запуска контейнеров
                    sh "docker-compose --env-file /var/jenkins_home/workspace/lmnad-jenkins/.env -f ${DOCKER_COMPOSE_FILE} up -d --build"
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
