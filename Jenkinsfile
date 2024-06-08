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
                // Копируем файл .env из указанной директории на хосте в текущую рабочую директорию Jenkins
                sh "cp ${ENV_FILE_PATH} ."
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    // Запуск docker-compose с использованием файла .env для сборки и запуска контейнеров
                    sh "docker-compose --env-file .env -f ${DOCKER_COMPOSE_FILE} up -d --build"
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
