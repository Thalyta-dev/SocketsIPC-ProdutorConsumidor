import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 10000


print("O ID do consumir é :", HOST)

            
soma =0               
cont = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST,PORT)) #Fazendo a conexão com o socket
    
    s.listen() #Ouvindo conexão, esperando para receber o cliente
    
    conn, addr = s.accept() #aceitando
    
    with conn:
        
        print("***"*10)
        print("Connected by", addr)
        print("***"*10)
        
        while True:
            
            data = conn.recv(1024)
            
            print("==="*16)
            print("consuming number...", data)
            print("==="*16)

            if  int(data) == 0:
                
                print("***"*6)
                print("Desconect")
                print("***"*6)
                conn.close()
                sys.exit()
                break

            
            for numero  in range(int(data)+1):
                
                print("Working...",)
              
                for i in range(2,numero):
                    condition = True        
            
                    if numero%i == 0:  
                        cont+=1
                        
                if cont == 0: 
                    soma = soma + numero
                cont =0

        conn.send(str(soma).encode('utf-8'))
                

