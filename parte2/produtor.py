import socket
import sys

HOST = input("Insira o IP: ")
PORT = 8080
number = 0

# Aqui criamos um objeto do tipo socket e definimos as caracteristicas dele, como o tipo de transmissão de dados que é TCP e também definimos que usaremos endereço da internet

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Aqui estamos definindo um socket que receberá conexões
s.bind((HOST, PORT))

# Aqui ele escutará um cliente que quer conectar
s.listen(1)

# O cliente faz um pedido para o servidor para conectar, e o servidor aceita a conexão
conn, addr = s.accept()

print(f"Conectado à {addr}")

# Aqui vamos fazer um While para receber os números enquanto o produtor não desconectar
while True:

    number = input("Digite um número: ")  # Recebe o número do usuário

    # Aqui ele está enviando o número que o usuário digitou
    conn.sendall(str(number).encode('utf-8'))

    # Aqui ele está recebendo do produtor o resultado encontrado
    dados = conn.recv(1024).decode()

    print("O número que o consumidor retornou foi: ", repr(dados))

    # Se ele recebeu um dado inválido, vai sair do while
    if int(dados) == 0:
        break

# Aqui ele encerra a conexão assim que sai do while
s.close()
print("Conexão fechada")
sys.exit()
