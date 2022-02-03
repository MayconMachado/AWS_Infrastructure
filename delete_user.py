import boto3

"""
Delete a user
"""


def iam_delete_user(username):
    # Create IAM client
    iam = boto3.client('iam')
    # Delete the user
    response = iam.delete_user(
        UserName=username
    )
    print(response)
    print("The user " + username + " was deleted!!!")
    return response
