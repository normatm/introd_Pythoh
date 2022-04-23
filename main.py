def print_hi(name):
    print(f'Hi, {name}')


def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2  # ( ** é o elevado ao quadrado)


def calcular_area_do_triangulo(lado, comprimento):
    return lado * comprimento/2


# Receber função para escrever

# Chamar função
# Ex. print_hi (Norma)
# Para salvar  Ctrl + S
# Para rodar  Run/Play para rodar
# f’no Hi = É um parâmetro de formatar
#   Ex. 	print (f’Hi,{name}’)
#	        print(‘Hi, ‘ + name)


# Estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Norma')
    print('Introdução ao Python na escola Iterasys que aprendeu as funções abaixo:')

    # Estrutura que já vem dividido em 3 partes.
    # 1 – Imports (Biblioteca/ Lista de Compra)
    # 2- Classe (que tem o nome do arquivo)
    # 3 - Métodos/ Funções
    # Métodos (só faz e fica quieto)
    # Funções (ele faz e dá retorno com valor)
    # def = definition = definição (é algo que cria algo)
    # () Os parênteses são variáveis que vai enviar e receber o nome.

    # Chamar função Area do Retângulo

    resultado = calcular_area_do_retangulo(3, 4)
    print(f'A area do retangulo e de {resultado} m²')

    # RESULTADO = A área do retângulo é de 12 m²

    # Chamar função Area do Quadrado

    resultado = calcular_area_do_quadrado(5)
    print(f'A area do quadrado e de {resultado} m²')

    # RESULTADO =  A área do quadrado é de 25 m²

    # Chamar função Area do Triangulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A area do triangulo e de {resultado} m²')

    # RESULTADO =  A área do triangulo é de 21.0 m²
