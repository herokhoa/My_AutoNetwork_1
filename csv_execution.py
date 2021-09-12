from csv import DictReader
from pprint import pprint
import paramiko
import time

conf_dict = {}
with open ('two_devives.csv', 'r') as csv_file:
    csv_content = DictReader(csv_file)
    column_names = csv_content.fieldnames
    # print(colum_names)
    for row in csv_content:
        for column_name in column_names:
            if not column_name:
                continue
            if not row[column_name]:
                continue
            if column_name not in conf_dict.keys():
                conf_dict[column_name] = []
            conf_dict[column_name].append(row[column_name])

pprint(conf_dict)
username = 'cisco'
password = 'cisco'
for ip in conf_dict.keys():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)

    print("Successful connection", ip)

    remote_connection = ssh_client.invoke_shell()
    print(f"\nExecuting Commands are \n{'~'*20}\n{conf_dict[ip]}")
    for conf in conf_dict[ip]:
        remote_connection.send(conf+'\n')
		 time.sleep(1)
        readoutput = remote_connection.recv(655350)
        print(readoutput.decode('ascii'))
        time.sleep(5)
    ssh_client.close