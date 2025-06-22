pipeline {
    agent {
        docker { image 'python:3.11' }
    }
    stages {
        stage('Clone Repository') {
            steps { git 'https://github.com/YourUsername/YourPythonRepo.git' }
        }
        stage('Install Streamlit') {
            steps { sh 'pip install streamlit' }
        }
        stage('Run Streamlit App') {
            steps { sh 'streamlit run main.py --server.headless true' }
        }
    }
}
