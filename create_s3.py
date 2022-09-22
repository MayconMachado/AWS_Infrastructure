import boto3

def create_s3(bucketname):
    client = boto3.client('s3')
    try:
        client.create_bucket(Bucket=bucketname,CreateBucketConfiguration={'LocationConstraint': 'sa-east-1',},)
        print('''
        The bucket ''' + bucketname + " Was created")
    except:
        print('''
    There was an error, try again!''')
    return