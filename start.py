import conn
import instances
option = 0
while option != 3:
    print('''
        Choose the EC2 Instance to start
        
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
    ec2 = conn.resource
    response = ec2.instances.filter(InstanceIds = ids).start()

    print("Your Instance was started!")
    break