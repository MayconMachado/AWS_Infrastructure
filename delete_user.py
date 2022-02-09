import boto3

"""
Delete a user
"""


def iam_delete_user(username):
    iam = boto3.client('iam')

    response = iam.delete_user(UserName=username)
    print("The user " + username + " was deleted!!!")
    return response
