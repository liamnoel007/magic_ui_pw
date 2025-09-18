pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'git@github.com:liamnoel007/magic_ui_pw.git', branch: 'main', credentialsId: 'github-ssh-key'
            }
        }
        stage('Setup Permissions') {
            steps {
                sh '''
                rm -rf allure-results
                mkdir allure-results
                chown 108:113 allure-results
                chmod 775 allure-results
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t magic-ui-pw-tests .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm --user 108:113 -v $(pwd)/allure-results:/app/allure-results magic-ui-pw-tests'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}