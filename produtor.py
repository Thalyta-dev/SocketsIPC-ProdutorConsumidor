import socket
import sys



HOST = socket.gethostbyname(socket.gethostname())
PORT = 10000

number = 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST,PORT)) #abrindo a conexão
    
    while True:
        
        print("==="*22)
        print("Ready for send a number for consumer, wainting number... ")
        print("==="*22)

        
        number  =input() #receber o número do usuário
        s.send(str(number).encode('utf-8'))
        data = s.recv(1024)
        
        if not data:
            
            print("***"*6)
            print("Connection closed")
            print("***"*6)
            
            s.close()
            sys.exit()
            break
        
        
        

   
            
            
            
        
        print("A number that consumer find: ", repr(data))   
   
