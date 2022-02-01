#Stop Instance
import conn
import instances

ec2 = conn.resource
ids = instances.gandalf

ec2.instances.filter(InstanceIds = ids).stop() #for stopping an ec2 instance

print("Your instance was stopped")
#ec2.instances.filter(InstanceIds = ids).terminate() #for terminating an ec2 instance