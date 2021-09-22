#Questão 1: Escreva um programa em que o usuário informa um ano (entre 1 e 3999) e o programa imprime este ano em algarismos romanos.

def nromanos():
    '''O PROGRAMA receberá um ano (entre 1 e 3999) e o programa imprime este ano em algarismos romanos'''

    print("Seja bem-vindo ao programa dos números romanos. Aqui você será capaz de converter um ano em algarismos arábicos (entre 1 e 3999) para algarismos romanos")

    n = int(input("Insira um número inteiro (entre 1 e 3999) para fazermos a conversão: "))

    if  n > 3999 or n < 1:
        return 'O número n não está entre 1 e 3999 !!'

    resultado = converter_romano(n)

    return resultado


def converter_romano(n):
    '''A função vai converter um número n (de 1 a 3999) no algarismo arábico
    para os algarismos romanos
    dados de entrada -> int
    dados de saída -> string'''
    
    arabico = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    romanos = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    resultado = []
 
    for i in range(len(arabico)):
        contador = int(n / arabico[i])
        resultado.append(romanos[i] * contador)
        n -= arabico[i] * contador
    return ''.join(resultado)

#Questão 2: Escreva um programa em que o usuário informa um número inteiro positivo e o programa imprime uma mensagem informando se o número é primo ou composto.

def p_primo():
    '''Programa para verificar se o número é primo ou composto'''

    print("Seja bem-vindo ao programa de verificação de números primos!\n")
    print("Aqui você será capaz de verificar se um determinado número inteiro e positivo é primo ou composto\n")

    n = int(input("Insira um número inteiro e positivo para fazermos a verificação: "))

    resultado = primo(n)

    return resultado

def primo (n):
    '''A função receberá um número inteiro e positivo e o programa retornará uma mensagem
    informando se o número n é primo ou composto
    dados de entrada -> int
    dados de saída -> string'''

    lista = [1,2,3,4,5,6,7,8,9,n]
    divisiveis = []
    if n >= 10:
        for i in lista:
            if n%i == 0:
                divisiveis.append(i)

        Q = len(divisiveis)
        if Q == 2:
            return 'Este número é primo!'

        else:
            return 'Este número é composto!'

    else:
        if n in [2,3,5,7]:
            return 'Este número é primo!'

        else:
            return 'Este número é composto!'

p_primo()

#Questão 3: Escreva um programa em que o usuário informa duas listas e o programa imprime uma nova lista com os elementos das duas listas iniciais intercalados.

    #Exemplo: se o usuário informa as listas [3, 6, 9, 12, 15] e ['a', 'b', 'c'], o programa deve imprimir a lista [3, 'a', 6, 'b', 9, 'c', 12, 15].

def programa_intercalar_listas():

    print("Seja Bem-Vindo ao programa! Aqui você você vai intercalar duas listas em uma única\n")

    x1 = input("Insira os dados da primeira lista separadas por vírgula: \n")
    x2 = input("Insira os dados da segunda lista separadas por vírgula: \n")

    lista1 = x1.split(',')
    lista2 = x2.split(',')
    
    return intercalar_listas(lista1,lista2)

def intercalar_listas(lista1, lista2):
    '''O programa vai intercalar os elementos de duas listas em um única lista
    dados de entrada -> lista, lista
    dados de saída -> lista'''

    novalista = []
    x1 = len(lista1)
    x2 = len(lista2)

    m = min(x1,x2)
    i = 0
    while i < m:
        novalista.append(lista1[0])
        del lista1[0]
        novalista.append(lista2[0])
        del lista2[0]

        i+=1

    x_1 = len(lista1)
    x_2 = len(lista2)

    if x_1 == 0:
        for i in lista2:
            novalista.append(i)

    else:
        for j in lista1:
            novalista.append(j)
        
    return novalista

#Questão 4: Faça o mesmo que na questão anterior, mas desta vez escrevendo uma função. Isto é, escreva uma função inter(L1,L2) que recebe duas listas L1 e L2 e retorna uma nova lista com os elementos de L1 e L2 intercalados. Não utilize variáveis globais (variáveis que não estão no interior de nenhuma função) nem coloque comandos fora das funções.

def intercalar_listas(lista1, lista2):
    '''A FUNÇÃO vai intercalar os elementos de duas listas em um única lista
    dados de entrada -> lista, lista
    dados de saída -> lista'''

    novalista = []
    x1 = len(lista1)
    x2 = len(lista2)

    m = min(x1,x2)
    i = 0
    while i < m:
        novalista.append(lista1[0])
        del lista1[0]
        novalista.append(lista2[0])
        del lista2[0]

        i+=1

    x_1 = len(lista1)
    x_2 = len(lista2)

    if x_1 == 0:
        for i in lista2:
            novalista.append(i)

    else:
        for j in lista1:
            novalista.append(j)
        
    return novalista

#Questão 5: Escreva um programa em que o usuário informa duas matrizes  3×3  e o programa imprime o produto dessas matrizes.

def p_produtomatriz():
    '''PROGRAMA p/ calcular o produto de duas matrizes 3x3'''
    
    print("Seja bem-vindo ao programa!Aqui você será capaz de realizar o produto entre duas matrizes 3x3.\n")

    x1 = input("Insira abaixo a primeira matriz com 3 elementos separadas por vírgula: \n")
    x2 = input("Insira abaixo a segunda matriz com 3 elementos separadas por vírgula: \n")

    
    lista1_string = x1.split(',')
    lista2_string = x2.split(',')

    #Limitando a função para admitir apenas matrizes 3x3
    if len(lista1_string) == 3 and len(lista2_string) == 3:
        
        #convertendo as listas de string p/ inteiros
        lista1 = []
        for i in lista1_string:
            x = int(i)
            lista1.append(x)

        lista2 = []
        for j in lista2_string:
            y = int(j)
            lista2.append(y)

        resultado = produtomatriz(lista1, lista2)
        
        return resultado

    else:
        return 'Uma ou mais matrizes possuem mais ou menos de 3 elementos! Por favor, refaça a função'
    
def produtomatriz(m1,m2):
    '''A função vai retornar o produto de duas matrizes 3x3
    dados de entrada -> lista, lista
    dados de saída -> lista'''
    produto = []

    for i in list(range(len(m1))):
        produto.append(m1[i]*m2[i])

    return produto

#Questão 6: Faça o mesmo que no item anterior, mas desta vez para matrizes quadradas quaisquer (não necessariamente  3×3 ).

def p_produtomatriz():
    '''PROGRAMA p/ calcular o produto de duas matrizes QUADRADAS'''
    
    print("Seja bem-vindo ao programa!Aqui você será capaz de realizar o produto entre duas matrizes QUADRADAS.\n")

    x1 = input("Insira abaixo a primeira matriz com 3 elementos separadas por vírgula: \n")
    x2 = input("Insira abaixo a segunda matriz com 3 elementos separadas por vírgula: \n")

    
    lista1_string = x1.split(',')
    lista2_string = x2.split(',')

    #AQUI ESTÁ A DIFERENÇA DA QUESTÃO 5 PARA A QUESTÃO 6
    #Limitando a função para admitir apenas MATRIZES QUADRADAS
    if len(lista1_string) != len(lista2_string):
        return 'Uma das matrizes possui uma quantidade de elementos diferente da outra! Insira apenas matrizes quadradas!'
    
    #convertendo as listas de string p/ inteiros
    lista1 = []
    for i in lista1_string:
        x = int(i)
        lista1.append(x)

    lista2 = []
    for j in lista2_string:
        y = int(j)
        lista2.append(y)

    resultado = produtomatriz(lista1, lista2)
    
    return resultado
    
def produtomatriz(m1,m2):
    '''A função vai retornar o produto de duas matrizes 3x3
    dados de entrada -> lista, lista
    dados de saída -> lista'''
    produto = []

    for i in list(range(len(m1))):
        produto.append(m1[i]*m2[i])

    return produto

#Questão 7: Elabore um programa em que o usuário deve fornecer um número natural n e o programa deve imprimir no console o triângulo de Pascal até a linha de número n (inclusive). Relembrando:

    #As linhas do triângulo de Pascal são numeradas a partir de 0;
    #A linha de número  i  do triângulo de Pascal possui  i+1  colunas, numeradas de 0 a  i ;
    #O elemento que ocupa a linha  i  e a coluna  j  do triângulo de Pascal corresponde ao número de combinações de  i  elementos  j  a  j  ( Cij ).

def programa_pascal():
    '''PROGRAMA p/ printar o triângulo de Pacal'''

    print("Olá! Seja bem-vindo ao programa Triângulo de Pascal!\n")
    print("Neste programa, você vai conseguir projetar no IDLE o Triângulo de Pascal\n\n")

    n = int(input("Insira um valor (n) inteiro referente a número da linha do triângulo: "))

    resultado = pascal(n)

    qtd_linhas = len(resultado)

    for i in resultado:
        print("", i)
        
      

def pascal(n):
    '''O programa receberá um número (n) e retornará o triângulo de Pascal até a linha (n) inclusive
    Dados de entrada -> int
    Dados de saída -> list'''   

    triangulo = []

    #indice (i) referente a linha
    for i in list(range(n+1)):
        if i == 0:
            triangulo.append([1])

        elif i == 1:
            triangulo.append([1,1])
            
        else:
            #indice j referente ao indice da linha i
            linha = []
            for j in list(range(i+1)):
                if j == 0:
                    linha.append(1)

                elif j == (i):
                    linha.append(1)
                    triangulo.append(linha)
                    
                else:
                    linha.append(triangulo[i-1][j-1] + triangulo[i-1][j])           
                
    return triangulo

