pipeline {
    agent {
        label 'generic'
    } //agent
    stages {
        stage("Setup script") {
            steps {
                sh """
                    pip install --upgrade pip
                    pip install pytest
                """
            } //steps
        } //stage
        stage("Run unit tests") {
            steps {
                sh """
                    python -m pytest
                """
            } //steps
        } //stage
        stage("Deploy to another server") {
            steps {
                sh """
                # // Package into rpm and upload
                """
            } //steps
        } //stage
    } //stages
    post {
        always {
            sh """
                sudo pip uninstall pytest -y
            """
        } //always
    } //post
} //pipeline