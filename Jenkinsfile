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

        stage('Copy .env file') {
            steps {
                script {
                    sh 'echo "DJANGO_SECRET_KEY=prod_local" > lmnad-jenkins/.env'
                    sh 'echo "DJANGO_SETTINGS_MODULE=project.settings.server" >> lmnad-jenkins/.env'
                    sh 'echo "DB_HOST=db" >> lmnad-jenkins/.env'
                    sh 'echo "DB_USER=lmnad_prod_local" >> lmnad-jenkins/.env'
                    sh 'echo "DB_PASSWORD=12345" >> lmnad-jenkins/.env'
                    sh 'echo "CELERY_BROKER_URL=amqp://guest:guest@broker:5672" >> lmnad-jenkins/.env'
                    sh 'echo "CELERY_RESULT_BACKEND=rpc://" >> lmnad-jenkins/.env'
                    sh 'echo "" >> lmnad-jenkins/.env' // Пустая строка между группами переменных
                    sh 'echo "MYSQL_ROOT_HOST=%" >> lmnad-jenkins/.env'
                    sh 'echo "MYSQL_ROOT_PASSWORD=78910" >> lmnad-jenkins/.env'
                    sh 'echo "" >> lmnad-jenkins/.env' // Пустая строка между группами переменных
                    sh 'echo "YANDEX_TRANSLATE_API_KEY=local" >> lmnad-jenkins/.env'
                    sh 'echo "GEOPOSITION_GOOGLE_MAPS_API_KEY=local" >> lmnad-jenkins/.env'
                }
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
