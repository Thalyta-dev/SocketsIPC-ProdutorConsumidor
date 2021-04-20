import socket
import sys


# Aqui a função recebe por parametro o número que o usuario digitou e soma os primos existentes nele
def somar_primos(dados_recebidos):
    soma = 0
    cont = 0

    print("Trabalhando...")
    for numero in range(int(dados_recebidos)+1):

        for i in range(2, numero):
            if numero % i == 0:
                cont += 1

        if cont == 0 and numero != 1:
            soma = soma + numero
        cont = 0
    return soma


HOST = input("Insira o IP: ")
PORT = 8080

# Aqui criamos um objeto do tipo socket e definimos as caracteristicas dele, como o tipo de transmissão de dados que é TCP e também definimos que usaremos endereço da internet
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Aqui ele vai pedir para conectar com o servidor
s.connect((HOST, PORT))

print(f"Conectado à: {s.getpeername()}")

# Aqui vamos fazer um while para receber os números enquanto não desconectar
while True:
    # Aqui ele está recebendo os números
    dadosRecebidos = s.recv(1024).decode()

    print("Número recebido: ", int(dadosRecebidos))

    # Caso o produtor tenha digitado 0, ele atribuirá um valor inválido
    if int(dadosRecebidos) == 0:
        break

    s.sendall(str(somar_primos(dadosRecebidos)).encode('utf-8'))

s.sendall(str(dadosRecebidos).encode('utf-8'))
s.close()
print("Conexão fechada")
sys.exit()
