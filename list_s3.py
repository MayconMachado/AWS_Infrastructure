import boto3
import pprint

def list_s3():
    client = boto3.client('s3')
    response = client.list_buckets()

    for x in response['Buckets']:
        pprint.pprint(x['Name'])
    return