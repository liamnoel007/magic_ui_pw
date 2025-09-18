pipeline {
    agent any

    environment {
        IMAGE_NAME = "magic-ui-pw-tests"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:liamnoel007/magic_ui_pw.git',
                    credentialsId: 'github-ssh-key'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    # Чистим старые результаты
                    rm -rf allure-results && mkdir allure-results

                    # Запускаем контейнер от имени Jenkins
                    docker run --rm \
                      -u \$(id -u jenkins):\$(id -g jenkins) \
                      -v ${WORKSPACE}/allure-results:/app/allure-results \
                      ${IMAGE_NAME}
                """
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
