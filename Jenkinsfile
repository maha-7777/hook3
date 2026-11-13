pipeline{
  agent any
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Build'){
      steps{
        echo 'Checking Python application'
        bat 'python -m py_compile app.py'
      }
    }
    stage('Test'){
      steps{
        echo 'Expecting automated tests'pipeline{
  agent any
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Build'){
      steps{
        echo 'Checking Python application'
        bat 'python -m py_compile app.py'
      }
    }
    stage('Test'){
      steps{
        echo 'Expecting automated tests'
        bat python -m unittest app'
      }
    }
    stage ('Run Application'){
      steps{
        bat 'python app.py'
      }
    }
        bat python -m unittest app'
      }
    }
    stage ('Run Application'){
      steps{
        bat 'python app.py'
      }
    }
      }
    post {
      success{
        echo 'CI Pipeline coompleted successfully'
      }
      failure {
        echo 'CI pipeline failed'
      }
    }
