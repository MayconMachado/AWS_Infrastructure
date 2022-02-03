import time
import pprint

option = 0
while option != 3:
    print('''
        Welcome to EC2 service manager!
        Enter the number corresponding to the option
        
        [ 1 ] Instances
        [ 2 ] Users
        [ 3 ] Exit
    ''')
    option = int(input("What is your choice? "))

    if option == 1:
        while option != 6:
            print('''
                Choose the desired action for EC2 Instances
                
                [ 1 ] Describe Instances
                [ 2 ] List Running Instances
                [ 3 ] Start Instance
                [ 4 ] Stop Instance
                [ 5 ] Reboot Instance
                [ 6 ] Return
            ''')
            option = int(input("What is your choice? "))
            if option == 1:
                import describe
                describe.response
            elif option == 2:
                import running
                #result = running()
                #print(result)
                running.response
            elif option == 3:
                import start
                start.response
            elif option == 4:
                import stop
                #stop.response
            elif option == 5:
                import reboot
                reboot.response
            else:
                print("Error, select corresponding number")
            time.sleep(2)

    elif option == 2:
        while option != 3:
            print('''
             Choose the desired action for EC2 Instances
                
                [ 1 ] List users 
                [ 2 ] Create new user
                [ 3 ] Delete user
            ''')
            option = int(input("What is your choice? "))
            if option == 1:
                import list_user
                list_user.response
            elif option == 2:
                import createuser
                createuser.response
            elif option == 3:
                import delete_user
                delete_user.iam_delete_user('IAM_USER_NAME')
            else:
                print("Error, select corresponding number")
            time.sleep(2)
    else:
        print("")
print("FIM")