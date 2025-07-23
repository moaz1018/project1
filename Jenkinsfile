pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {
       stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/moaz1018/project1.git'
    }
}

        stage('Check Python Version') {
            steps {
                sh "${env.PYTHON} --version"
            }
        }

        stage('Install Streamlit') {
            steps {
                sh "${env.PYTHON} -m pip install --upgrade pip"
                sh "${env.PYTHON} -m pip install streamlit"
            }
        }

        stage('Show Streamlit Version') {
            steps {
                sh "${env.PYTHON} -m streamlit --version"
            }
        }

        stage('Run Streamlit App') {
            steps {
                sh "nohup ${env.PYTHON} -m streamlit run main.py --server.headless true --server.port=8501 &"
            }
        }

        stage('Access Info') {
            steps {
                script {
                    def ip = sh(script: "curl -s http://checkip.amazonaws.com", returnStdout: true).trim()
                    echo "🌐 Access your Streamlit app at: http://${ip}:8501"
                }
            }
        }
    }
}
