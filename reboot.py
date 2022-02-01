#Reboot Instance
import conn

ec2 = conn.client
response = ec2.reboot_instances(InstanceIds=['i-0edea84bd8d6ddd10'],)
print(response)
