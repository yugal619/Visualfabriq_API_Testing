pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                     bat 'python --version'
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
