import boto3
# Create IAM client

def create_user(username):
    iam = boto3.client('iam')

    response = iam.create_user(UserName=username)
    print("The user " + username + " was created!!!")
    return response

