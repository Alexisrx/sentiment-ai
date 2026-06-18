stage('Lint') {
            steps {
                sh '''
                    docker run --rm \
                    -v $WORKSPACE:/app \
                    -w /app \
                    python:3.12-slim \
                    sh lint.sh
                '''
            }
        }