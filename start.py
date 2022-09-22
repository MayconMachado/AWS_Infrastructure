import conn
import instances

def start():
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
            response = ec2.instances.filter(InstanceIds = ids).start()
            print("Your Instance was started!")
            break
        except:
            print('''
    There was an error, try again!''')
    return