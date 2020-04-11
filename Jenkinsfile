pipeline {
    agent {
        label 'generic'
    } //agent
    stages {
        stage("Setup script") {
            steps {
                sh """
                    sudo pip3 install --upgrade pip
                    sudo pip3 install pytest
                """
            } //steps
        } //stage
        stage("Run unit tests") {
            steps {
                sh """
                    sudo python3 -m pytest
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