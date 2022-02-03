
#def running ():
import conn
import pprint
ec2 = conn.resource
client = conn.client

instances = ec2.instances.filter(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ],
)
for instance in instances:
    print(instance.id, instance.instance_type, instance.tags)
    response = client.reboot_instances(InstanceIds=[instance.id], DryRun=False)
    #pprint.pprint(response)
    #return response