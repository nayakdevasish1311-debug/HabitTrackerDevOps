
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Habit Tracker source code'
                bat 'git --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Habit Tracker V3 Docker image'
                bat 'docker build -t devashis1311/habit-tracker:v3 .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                bat 'docker images devashis1311/habit-tracker'
            }
        }
    }
}
