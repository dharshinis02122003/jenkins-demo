#program 1
print("Hello from Jenkins!")
pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                bat 'python hello.py'
            }
        }
    }
}
