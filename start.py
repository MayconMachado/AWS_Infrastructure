import conn
import instances
ids = instances.gandalf
ec2 = conn.resource

ec2.instances.filter(InstanceIds = ids).start()

print("Your Instance was started!")