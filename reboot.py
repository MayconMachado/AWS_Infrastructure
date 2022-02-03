#Reboot Instance
import conn
import instances
option = 0
while option != 3:
    print('''
        Choose the EC2 Instance to reboot
        
        [ 1 ] Gandalf
        [ 2 ] Balrog
        [ 3 ] Return
    ''')
    option = int(input("What is your choice? "))
    if option == 1:
        ids = instances.gandalf
    elif option == 2:
        ids = instances.balrog
    else:
        print("")
        break
    ec2 = conn.client
    response = ec2.reboot_instances(InstanceIds = ids,)
    print("Your Instance was rebooted")
