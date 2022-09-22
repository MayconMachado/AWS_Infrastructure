import boto3

def delete_s3(bucketname):
    client = boto3.client('s3')
    try:
        client.delete_bucket(Bucket=bucketname,)
        print('''
    The bucket ''' + bucketname + " Was deleted!!!")
    except:
        print('''
    This Bucket doesn't exist !''')

    return