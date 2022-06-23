import socket
import json
from Simulador_emprestimos import *

#Instanciar o objeto socket do servidor na família internet e do tipo TCP.
socket_servidor = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

#Associação do socket do servidor a uma porta e o endereço da minha máquina.
host = socket.gethostname()
porta = 6666

#Preparar o socket para ser utilizado na apliação através da porta e do endereço atribuidos ao socket.
socket_servidor.bind((host, porta))

socket_servidor.listen(5)

while True:
    #Comunicação estabelecida.
    socket_cliente, addr = socket_servidor.accept()
    print ('Conectado com {}' .format(addr) )

    # Enquanto a conexão estiver estabelecida, o cliente poderá fazer quantas consultas quiser.
    # Por isso precisaremos de 2 whiles. Um para manter o accept() e outra para controlar o recebimento
    # das opções escolhidas pelo cliente e, assim manter o servidor trabalhando até que o cliente escolha a opção 2 (SAIR).
    while True:
        opcao = socket_cliente.recv(2048)
        opcao = (opcao.decode('ascii'))

        if (opcao == '1'):
            
            print ('Processando os dados recebidos...')

            # Receber e Deserializar os dados recebidos do Clliente para realizar as operações.
            dados = socket_cliente.recv(2048)
            dados = json.loads(dados.decode('ascii'))

            # Atribuição dos valores e dos tipos de dados decodificados e associá-los em variáveis locais do código do Servidor.
            # Para trabalhar com os mesmos...
            valor_emprestimo = float (dados[0])
            tempo_pagamento = int (dados[1])
            taxa_juro = float (dados[2])

            #Instanciando o objeto simulador_empréstimo.
            s_emprestimo = Simulador_emprestimos(valor_emprestimo, tempo_pagamento, taxa_juro)

            #Associar os valores retornados dos métodos invocados à variaveis locais.
            parcela = s_emprestimo.parcelas()
            juro_efetivo = s_emprestimo.juros()

            #Serializar para enviar os resultados da aplicação do servidor para o cliente.
            resultados = [parcela, juro_efetivo]
            resultados = json.dumps(resultados)
            socket_cliente.send(resultados.encode('ascii'))

            #Destruir s_emprestimo
            del s_emprestimo
        
        #Se opção for igual a 2 a comunicação entre Servidor e Cliente conectado será encerrada.
        elif opcao == '2':
            socket_cliente.close()
            print ('Comunicação com {} encerrada!'.format(addr))
            break