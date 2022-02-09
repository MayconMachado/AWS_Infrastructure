import conn

def describe():
    ec2 = conn.client
    response = ec2.describe_instances()
    for i in response['Reservations']:
        print(''' ''')
        for printout in i['Instances']:
            for x in printout['Tags']:
                print("NAME: " + x['Value'])

            a = printout['State']
            print("STATUS: " + a['Name'])

            print("ID: " + printout['InstanceId'])
            print("TYPE: " + printout['InstanceType'])
            print('CREATED: ' + str(printout['LaunchTime']))
            print("IP: " + printout['PrivateIpAddress'])



