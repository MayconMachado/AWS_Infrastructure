#Reboot Instance
import conn
import instances
import time

def reboot():
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
            elif option == 3:
                break
            else:
                print("Error, select corresponding number")
                break
            time.sleep(2)
            ec2 = conn.client
            response = ec2.reboot_instances(InstanceIds = ids,)
            print("Your Instance was rebooted")
        except:
            print('''
    There was an error, try again!''')
    return

