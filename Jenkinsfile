pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python --version'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
