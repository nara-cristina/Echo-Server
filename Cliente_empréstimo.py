import socket
import json
import time

# Intanciar o socket cliente.
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dados do endereço do servidor para que o socket cliente saiba com quem vai se conectar.
host = socket.gethostname()
porta = 6666

socket_cliente.connect((host, porta))

#Saudação
print ('\n*=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=*')
print(' \33[1;30;41m BEM VINDO AO NOSSO SIMULADOR DE EMPRÉSTIMOS! \33[m ')
time.sleep(1)
print(''' \33[1;33m Descrição do serviço:\33[m \33[1;31m Caro cliente, este software calcula o valor das parcelas 
          e o juro efetivo referente ao seu empréstimo efetuado através do seu banco. \33[m''')
print ('*=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=*')
time.sleep(3)

print ('\n \33[1;30;41m Inicializando...\33[m \n')
time.sleep(3)

opcao = '0'

#Menu para identificar as escolhas do usuário...
#Enquanto a poção for diferente de 2 (sair=encerrar comunicação), o programa retornará sempre para o menu.
#Afim de receber os novos comandos estabelecidos através da escolha do cliente.
while opcao != '2':
    print ('*=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=* ')
    print('\33[1;33m ESCOLHA UMA OPÇÃO: \33[m')
    print (' \33[1;31m [1] ENVIAR SEUS DADOS \n  [2] SAIR  \33[m')
    print('*=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=* \n ')
    opcao =  input ('\33[1;33m OPÇÃO = \33[m ')
    socket_cliente.send(opcao.encode('ascii'))

    #Se a opção for igual a 1, o cliente precisa enviar os dados do empréstimo para o Servidor 
    #para que este realize seu serviço.
    if (opcao == '1'):
        valor_emprestimo = input('\33[1;33m Valor do Empréstimo = R$ ')
        tempo_pagamento = input(' Tempo de Pagamento (meses) = ')
        taxa_juro = input(' Taxa de Juro (Por favor, insira apenas a parte numérica) =   \33[m')
        print ('*=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=* ')
        print ('\n \33[1;30;41m Estamos processando seus dados... Aguarde... \33[m \n')
        time.sleep (2)

        # Em uma variável armazena uma lista com os valores de entrada do cliente.
        dados = [valor_emprestimo, tempo_pagamento, taxa_juro]

        # O método dumps serializa os valores para poder enviar os dados para o servidor através da rede de uma só vez.
        dados = json.dumps(dados)

        # Enviar os dados obtidos do cliente para o servidor contactado.
        socket_cliente.send(dados.encode('ascii'))

        # Receber os resultados dos cálculos do servidor:
        resultados = socket_cliente.recv(2048)

        # Desserializar e decodificar a mensagem:
        resultados = json.loads(resultados.decode('ascii'))

        #Atribuir cada valor à uma variável local, afim de identificar e guardar o dados 
        #em seus respectivos significados.
        valor_parcela = resultados[0]
        juro_efetivo = resultados[1]

        print('\33[1;30;43m Valor da parcela = R$ {:.2f} \33[m' .format(valor_parcela))
        print('\33[1;30;43m Juro efetivo = {:.2f} %  \33[m \n'.format(juro_efetivo))
        time.sleep(2)

    #Opção para caso o cliente digite qualquer coisa que fors diferente 
    #das opções do menu.
    elif (opcao != '1') and (opcao != '2'):
        print(' \33[1;30;41m OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE.\33[m \n ')
        time.sleep(2)

    #Caso opção for igual a 2, comunicação entre Cliente e Servidor desfeita.
    else:
        print('\n \33[1;30;41m AGRADECEMOS SUE ACESSO, CARO CLIENTE! \33[m')
        socket_cliente.close()
        break
