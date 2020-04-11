pipeline {
    agent {
        label 'generic'
    } //agent
    stages {
        stage("Setup script") {
            steps {
                sh """
                    pip3 install --upgrade pip3
                    pip3 install pytest
                """
            } //steps
        } //stage
        stage("Run unit tests") {
            steps {
                sh """
                    python3 -m pytest
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
                sudo pip3 uninstall pytest -y
            """
        } //always
    } //post
} //pipeline