#conection file
import boto3

client = boto3.client('ec2')
resource = boto3.resource('ec2')
iam = boto3.client('iam')

#S3

client_s3 = boto3.client('s3')