pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.prod.local.yml'
        WORKSPACE_DIR = '/var/jenkins_home/workspace/lmnad-jenkins' // Путь к вашей рабочей директории
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
                    sh "mkdir -p ${WORKSPACE_DIR}" // Создаем рабочую директорию, если ее еще нет
                    sh 'echo "DJANGO_SECRET_KEY=prod_local" > ${WORKSPACE_DIR}/.env'
                    sh 'echo "DJANGO_SETTINGS_MODULE=project.settings.server" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "DB_HOST=db" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "DB_USER=lmnad_prod_local" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "DB_PASSWORD=12345" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "CELERY_BROKER_URL=amqp://guest:guest@broker:5672" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "CELERY_RESULT_BACKEND=rpc://" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "" >> ${WORKSPACE_DIR}/.env' // Пустая строка между группами переменных
                    sh 'echo "MYSQL_ROOT_HOST=%" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "MYSQL_ROOT_PASSWORD=78910" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "" >> ${WORKSPACE_DIR}/.env' // Пустая строка между группами переменных
                    sh 'echo "YANDEX_TRANSLATE_API_KEY=local" >> ${WORKSPACE_DIR}/.env'
                    sh 'echo "GEOPOSITION_GOOGLE_MAPS_API_KEY=local" >> ${WORKSPACE_DIR}/.env'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    // Запуск docker-compose с использованием файла .env для сборки и запуска контейнеров
                    sh "docker-compose -f ${WORKSPACE_DIR}/${DOCKER_COMPOSE_FILE} up -d --build"
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
