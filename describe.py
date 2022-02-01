import pprint

import conn

print("1_________________________________________________________________________ ")

ec2 = conn.client
response = ec2.describe_instances()
reserv = response['Reservations']
reserv2 = response['ResponseMetadata']
#print(reserv)
#print(reserv2)
pprint.pprint(response)

print("2_________________________________________________________________________ ")

ec2 = conn.resource
for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)

