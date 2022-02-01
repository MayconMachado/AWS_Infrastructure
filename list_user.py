#List users IAM
import pprint
import conn

iam = conn.iam
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    pprint.pprint(response)