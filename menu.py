import time
import delete_s3
import describe
import list_s3
import running
import start
import stop
import reboot
import createuser
import list_user
import delete_user
import create_s3

option = 0
while option != 4:
    print('''
    -------------------------------------------------------------
    *       Welcome to EC2 service manager!                     *
    *       Enter the number corresponding to the option        *
    *                                                           *
    *       [ 1 ] EC2 Instances                                 *
    *       [ 2 ] IAM Users                                     *
    *       [ 3 ] S3                                            *
    *       [ 4 ] Exit                                          *
    -------------------------------------------------------------
    ''')

    try:
        option = int(input("What is your choice? "))
    except ValueError:
        print('''
    Whrite a valid number!!!''')
    if option == 1:
        while option != 6:
            print('''
    -------------------------------------------------------------
    *       Choose the desired action for EC2 Instances         *
    *                                                           *
    *       [ 1 ] Describe Instances                            *
    *       [ 2 ] List Running Instances                        *
    *       [ 3 ] Start Instance                                *
    *       [ 4 ] Stop Instance                                 *
    *       [ 5 ] Reboot Instance                               *
    *       [ 6 ] Return                                        *
    *       [ 7 ] Exit                                          *
    -------------------------------------------------------------
    ''')

            try:
                option = int(input("What is your choice? "))
            except ValueError:
                print('''
    Write a valid number''')

            if option == 1:
                describe.describe()
            elif option == 2:
                running.running()
            elif option == 3:
                start.start()
            elif option == 4:
                stop.stop()
            elif option == 5:
                reboot.reboot()
            elif option == 6:
                print('''
    Back to last menu...''')
            elif option == 7:
                print(''' 
                 Thanks for using 
                ------- END -------
                ''')
                exit()

            else:
                print('''
    Error, select corresponding number''')
            time.sleep(2)

    elif option == 2:
        while option != 4:
            print('''
    -------------------------------------------------------------
    *       Choose the desired action for IAM Users             *
    *                                                           *
    *       [ 1 ] List users                                    *
    *       [ 2 ] Create new user                               *
    *       [ 3 ] Delete user                                   *
    *       [ 4 ] Return                                        *
    *       [ 5 ] Exit                                          *
    -------------------------------------------------------------
    ''')

            try:
                option = int(input("What is your choice? "))
            except ValueError:
                pass

            if option == 1:
                list_user.list_user()
            elif option == 2:
                try:
                    user = str(input('''
    Write a name to Create: '''))
                    createuser.create_user(user)
                except:
                    print('''
    There was an error, try again!''')

            elif option == 3:
                try:
                    user = str(input('''
    Write a name to delete: '''))
                    delete_user.iam_delete_user(user)
                except:
                    print('''
    There was an error, try again!''')

            elif option == 4:
                print('''
    Back to last menu...''')

            elif option == 5:
                print(''' 
                  Thanks for using 
                ------- END -------
                ''')
                exit()
            else:
                print("Error, select corresponding number")
            time.sleep(2)
        option = 0

    elif option == 3:
        while option != 4:
            print('''
    -------------------------------------------------------------
    *       Choose the desired action for S3 Buckets            *
    *                                                           *
    *       [ 1 ] List S3 Buckets                               *
    *       [ 2 ] Create new Bucket                             *
    *       [ 3 ] Delete Bucket                                 *
    *       [ 4 ] Return                                        *
    *       [ 5 ] Exit                                          *
    -------------------------------------------------------------
    ''')

            try:
                option = int(input("What is your choice? "))
            except ValueError:
                pass

            if option == 1:
                list_s3.list_s3()

            if option == 2:
                try:
                    bucketname = input(str("Write a name of new bucket: "))
                except ValueError:
                    print('''
    Write a valid number!!!''')
                create_s3.create_s3(bucketname)

            if option == 3:
                try:
                    bucketname = input(str('''
    Write a name of the bucket to delete: '''))
                except ValueError:
                    print('''
    Write a valid number!!!''')
                delete_s3.delete_s3(bucketname)

            if option == 4:
                print('''
    Back to last menu...''')
            if option == 5:
                print(''' 
                 Thanks for using 
                ------- END -------
                ''')
                exit()
            time.sleep(2)
        option = 0
    else:
        print(''' 
         Thanks for using 
        ------- END -------
        ''')
        exit()
