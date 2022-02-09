#List users IAM
import conn

def list_user():
    iam = conn.iam

    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        result = response['Users']
        for x in result:
            print(x['UserName'])
    return