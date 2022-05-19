pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                withCredentials([
                    usernamePassword(credentialsId: 'AWS_CREDENTIALS',
                    usernameVariable: 'username',
                    passwordVariable: 'password')
                ]){
                    sh 'python3 script.py $username $password $InstanceType $VPCCidr $PublicCidr $PrivateCidr $BucketName $StackName'
                }
            }
        }
    }
}