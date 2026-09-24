pipeline {
    agent any

    parameters {
        string(name: 'COURSE_NAME', defaultValue: 'DevOps Engineering', description: 'Name of the course')
        string(name: 'STUDENT_COUNT', defaultValue: '45', description: 'Number of students enrolled')
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Generate Report') {
            steps {
                script {
                    // Print the required built-in variables
                    echo "=========================================="
                    echo "BUILD NUMBER: ${env.BUILD_NUMBER}"
                    echo "JOB NAME: ${env.JOB_NAME}"
                    echo "WORKSPACE: ${env.WORKSPACE}"
                    echo "=========================================="

                    // Run the Python script with parameter inputs
                    sh "python3 app.py '${params.COURSE_NAME}' '${params.STUDENT_COUNT}'"
                }
            }
        }

        stage('Archive Report') {
            steps {
                // Archive the artifact and enable fingerprinting
                archiveArtifacts artifacts: 'build_report.txt', fingerprint: true
            }
        }
    }
}
