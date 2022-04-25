# 1 – Imports (Biblioteca/ Lista de Compra)
# 2- Classe (que tem o nome do arquivo)

def print_hi(name):
    print(f'Hi, {name}')


def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2  # ( ** é o elevado ao quadrado)


def calcular_area_do_triangulo(lado, comprimento):
    return lado * comprimento / 2


def contagem_progressiva(fim):
    for numero in range(fim):  # repetir o bloco de zero até o fim
        print(numero)


def apoiar_candidato(nome, vezes):
    for numero in range(vezes):              # repetir quantas vezes apoia o candidato
    #contador = numero + 1
    # print(f'{contador} - {nome}')          # exibir o nome do candidato

        if numero < 10:
            print(f'0{numero+1}, -  {nome}')
        elif numero < 9:
            print(f'0{numero} + 1 - {nome}')
        else:
            print(numero+1, '-',nome)


#def brincar_de_plim(fim):
	#for numero in range(fim):      # brincadeira igual do Silvio Santos
		#if  numero % 4 == 0:      # % não calcula percentual e sim calcula o que sobra
            #print('PLIM!')
        #else:
            #print('{:0>3}'.format(numero))


def exibir_menu(resposta):
    opcao = {
        1: print_hi('Norma'),
        2: calcular_area_do_retangulo(8, 9),
        3: calcular_area_do_quadrado(7),
        4: calcular_area_do_triangulo(5, 4),
        5: contagem_progressiva(10),
        6: apoiar_candidato('Sabado', 10),
        7: sair()
    }
    return opcao.get(escolha, 'Opçao Invalida')

    # Receber função para escrever

# Chamar função
# Ex. print_hi (Norma)
# Para salvar  Ctrl + S
# Para rodar  Run/Play para rodar
# f’no Hi = É um parâmetro de formatar
#   Ex. 	print (f’Hi,{name}’)
#	        print(‘Hi, ‘ + name)


# Estrutura de identificação / execução do script  # Abaixo exemplo de Laço condicional
if __name__ == '__main__':



    resposta = "C"   #(variaveis que podem ser sim, verdadeiro, falso)

    while resposta.upper() != 'Z':

        print('######################################')
        print('#                                    #')
        print('#     MENU DE OPÇOES                 #')
        print('#    1- Olá Usuario                  #')
        print('#    2- Area do Retângulo            #')
        print('#    3- Area do Quadrado             #')
        print('#    4- Area do Triangulo            #')
        print('#    5- Contagem Progressiva         #')
        print('#    6- Apoiar Candidato             #')
        print('#                                    #')
        print('#    Z- Sair                        #')
        print('#                                    #')
        print('######################################')

        resposta = input("Escolha sua opçao")
        print(f'A sua escolha foi: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Norma')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print(f'A area do retangulo é de {resultado} m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(6)
                print(f'A area do quadrado é de {resultado} m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,8)
                print(f'A area do triangulo é de {resultado} m²')
            elif resposta == '5':
                contagem_progressiva(10) # fez a contagem regressiva de o a 9
            elif resposta == '6':
                 apoiar_candidato('Murphy',13) #mostrou o nome Murphy por 13 vezes
            else:
                print('Voce digitou uma opcao invalida. Escolha uma opçao de 1 a 7')
        else:
                print('Voce escolheu Sair. Volte Sempre!')
