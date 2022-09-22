#Stop Instance
import conn
import instances

def stop():
    option = 0
    while option != 3:
        print('''
    -------------------------------------------------------------
    *       Choose the EC2 Instance to reboot                   *
    *                                                           *
    *       [ 1 ] Gandalf                                       *
    *       [ 2 ] Balrog                                        *
    *       [ 3 ] Return                                        *
    -------------------------------------------------------------
    ''')
        try:
            option = int(input("What is your choice? "))
        except ValueError:
            pass
        try:
            if option == 1:
                ids = instances.gandalf
            elif option == 2:
                ids = instances.balrog
            else:
                print("")
                break
            ec2 = conn.resource
            response = ec2.instances.filter(InstanceIds = ids).stop()
            print("Your instance was stopped")
            break
            #ec2.instances.filter(InstanceIds = ids).terminate() #for terminating an ec2 instance
        except:
            print('''
    There was an error, try again!''')
    return