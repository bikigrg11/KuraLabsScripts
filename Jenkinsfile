pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
      sh 'echo "HELLO B2"'
      sh '''
        echo "This is B2"
        ls -lh
        '''
      }
    }
    stage ('test') {
      steps {
      sh 'echo "HELLO TEST"'
      sh '''
        echo "This list current dir"
        pwd
        '''
      }
    }

  }
}
