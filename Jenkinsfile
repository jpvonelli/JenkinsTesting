pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pytest'
            }
        }
    }
  post
  {
   always
   {
      sh 'echo "\n\n\n\nbye\n\n\n\n"'
   }
 }
}
