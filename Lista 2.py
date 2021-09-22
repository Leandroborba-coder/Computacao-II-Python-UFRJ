#Questão 1: Suponha que o país A tem uma população de 80 mil pessoas e uma taxa de crescimento anual da sua população de  3% . Já o país B tem uma população de 200 mil pessoas e taxa de crescimento anual de  1,5% . Escreva um programa que calcule e imprima a quantidade de anos necessária para que a população do país A se torne maior ou igual à população do país B.

def main():
    print("Seja Bem-Vindo ao programa de crescimento populacional!\n\n")
    print("Este programa calculará a quantidade de anos necessária para que a população\ndo país A - de 80 mil habitantes - com uma taxa de crescimento de 3% ultrapassará ou se igualará a população\ndo país B - de 200 mil habitantes - com uma taxa de crescimento de 1,5% ao ano.\n\n")

    resultado = populacao(80000,0.03,200000,0.015)

    x = input("Pressione o botão Enter para começar:\n")
    
    print("Serão necessários " + str(resultado) + " anos para que a população do país A ultrapasse a população do pais B.")
    
    
def populacao(pop1, taxa1, pop2, taxa2):
    '''A função vai calcular o ano em uma determinada população, com sua respectiva
    taxa de crescimento, ultrapassará a quantidade da população do segundo país.

    OBS.: INSIRA O VALOR DA TAXA EM DECIMAL. SE A TAXA FOR DE 10%, DIGITE 0.1
    
    dados de entrada -> int, float, int, float
    dados de saída -> int'''

    if pop1 <= pop2 and taxa1 > taxa2:
        ano = 1
        p1 = pop1
        p2 = pop2
        while p1 < p2:
            p1 = p1*(1+taxa1)
            p2 = p2*(1+taxa2)

            ano += 1

        return ano

    elif pop2 <= pop1 and taxa2 > taxa1:
        ano = 1
        p1 = pop1
        p2 = pop2
        while p2 < p1:
            p1 = p1*(1+taxa1)
            p2 = p2*(1+taxa2)

            ano += 1

        return ano
    
    else:
        return 'Essa condição é impossível de acontecer. Uma população jamais ultrapassará a outra'

#Questão 2: Faça o mesmo que na questão anterior, mas desta vez de forma genérica. Isto é, escreva uma função populacao(pop1,taxa1,pop2,taxa2) que recebe a população dos dois países em pop1 e pop2 e as taxas de crescimento dos dois países em taxa1 e taxa2 e retorna a quantidade de anos necessária para que a população do primeiro país se torne maior ou igual à população do segundo país.

def populacao(pop1, taxa1, pop2, taxa2):
    '''A função vai calcular o ano em uma determinada população, com sua respectiva
    taxa de crescimento, ultrapassará a quantidade da população do segundo país.

    OBS.: INSIRA O VALOR DA TAXA EM DECIMAL. SE A TAXA FOR DE 10%, DIGITE 0.1
    
    dados de entrada -> int, float, int, float
    dados de saída -> int'''

    if pop1 <= pop2 and taxa1 > taxa2:
        ano = 1
        p1 = pop1
        p2 = pop2
        while p1 < p2:
            p1 = p1*(1+taxa1)
            p2 = p2*(1+taxa2)

            ano += 1

        return ano

    elif pop2 <= pop1 and taxa2 > taxa1:
        ano = 1
        p1 = pop1
        p2 = pop2
        while p2 < p1:
            p1 = p1*(1+taxa1)
            p2 = p2*(1+taxa2)

            ano += 1

        return ano
    
    else:
        return 'Essa condição é impossível de acontecer. Uma população jamais ultrapassará a outra'

populacao(400000,.015,80000,.01)

#Questão 3: Escreva uma função transp(M) que recebe uma matriz M e retorna a matriz transposta.
def transp(matriz):
    '''A função irá receber uma matriz e retornará a matriz transporta
    dados de entrada -> lista
    dados de saída -> lista'''


    Qlinha = len(matriz)
    Qcoluna = len(matriz[0])

    resultado = []
    
    for i in list(range(Qcoluna)):
        linha = []
        for j in list(range(Qlinha)):        
            linha.append(matriz[j][i])

        resultado.append(linha)

    return resultado


transp([[1,2,4,5],[3,4,9,10],[5,6,11,12]])

#Questão 4: Escreva uma função freq1(s) que recebe uma string s e retorna um dicionário onde as chaves são as palavras que aparecem na string s e os respectivos valores são a quantidade de vezes que cada palavra aparece na string.

    #Exemplo: Se s = 'uma banana boa eh uma banana madura', então a função deve retornar um dicionário como {'uma' : 2, 'banana' : 2, 'boa' : 1, 'eh' : 1, 'madura' : 1}.

def freq1(s):
    '''A função contará a quantidade que cada palavra foi repetida em uma frase, retornando
    um dicionário com a palavra:quantidade
    dados de entrada -> string
    dados de saída -> dicionário'''

    frase_separada = s.split()

    dicionario = {}

    for i in frase_separada:
        Q = frase_separada.count(i)

        dicionario[i] = Q        

    return dicionario

freq1('uma banana boa eh uma banana madura')

#Questão 5: Escreva uma função freq2(s) que reebe uma string s e retorna um dicionário onde as chaves são os caracteres que aparecem na string s e os respectivos valores são a quantidade de vezes que cada caractere aparece na string.

    #Exemplo: Se s = 'banana boa', então a função deve retornar um dicionário como {'b' : 2, 'a' : 4, 'n' : 2, ' ' : 1, 'o' : 1}.

def freq2 (s):
    '''A função retornará um dicionário com a os caracteres usados em uma string e com suas
    respectivas quantidades de que foram usadas na frase (s)
    dados de entrada -> string
    dados de saída -> dicionário'''
    dicionario = {}

    for i in s:
        Q = s.count(i)

        dicionario[i] = Q
        
    return dicionario

#Questão 6: Escreva uma função custo(L,D) que recebe uma lista de compras L (uma lista de strings) e um dicionário D, onde as chaves são os produtos vendidos no mercado e os respectivos valores são os preços de cada produto, e retorna o preço total da compra dada pela lista L.

    #Exemplo: Se L = ['banana','maca','pessego'] e D = {'guarana' : 5.5, 'maca' : 11.9, laranja' : 4.9, 'banana' : 3.15, 'matte' : 4.8, 'pessego' : 13.4, 'agua' : 2.6}, a função deve retornar 28.45.

def custo (L,D):
    '''A função receberá uma lista de compras (L) e um dicionário
    e retornará a soma dos preços dos produtos comprados
    dados de entrada -> lista, dicionário
    dados de saída -> float'''

    total = 0
    for i in L:
        valor = D[i]
        total += valor

    return round(total,2)

#Questão 7: Seja D um dicionário de afinidades, isto é, um dicionário onde as chaves são nomes de pessoas e os respectivos valores são listas que contém o nome de todos de quem aquela pessoa gosta. Por exemplo, se Maria gosta de João e de Ana, uma entrada no dicionário D será 'Maria' : ['Joao', 'Ana']. Escreva uma função amigos(D) que recebe um dicionário de afinidades D e retorna uma lista de pares que representam as pessoas que se gostam mutuamente.

    #Exemplo: Se D = {'Maria' : ['Joao', 'Ana'], 'Pedro' : [], 'Ana' : ['Maria', 'Pedro', 'Carlos'], 'Joao' : ['Pedro', 'Carlos'], 'Carlos' : ['Ana', 'Maria', 'Pedro']}, então a função deverá retornar a lista [('Maria','Ana'),('Ana','Carlos')].

def amigos(D):
    '''A função verificará quais são as pessoas que se consideram amigas mutuamente
    dados de entrada -> dicionário
    dados de saída -> lista'''

    pessoas = []
    #Extraindo uma lista com todos as pessoas envolvidas
    for i in D:
        pessoas.append(i)
    
    amigos = []
    #Estrtura que vai extrair as amizades em comum, porém com resultados duplicados
    for j in D:
        for k in D[j]:
            for g in pessoas:
               if g in k:
                   amigos.append((g,j))


    resultado = []
    #EstruturaS para retirar os resultados duplicados
    for i in amigos:
        for j in amigos[1:]:
            if i[0] == j[1] and j[0] == i[1]:
                resultado.append(i)

    for t in resultado:
        for g in resultado[1:]:
            if t[0] == g[1] and g[0] == t[1]:
                posicao = resultado.index(g)
                del(resultado[posicao])
                
    return resultado            

#Questão 8: Suponha que temos um módulo chamado Mod. Explique a diferença que ocorre quando o carregamos em um programa utilizando cada uma das opções de comando abaixo (escreva a resposta no comentário que está no campo de código abaixo):

    #import Mod
    #from Mod import *

"""
Quando fazemos a importação de um módulo escrevendo "from Mod import * ", nós tornamos o código mais sucinto, já que não será necessário referencia o módulo
em todas as vezes que chamarmos a função. Veja abaixo um exemplo:

from math import *

def calculando (x):
    return x*pi

Quando nós fazemos a importação escrevendo "import Mod", nós somos obrigado a referenciar sempre o módulo em uma operação. Vejo o exemplo abaixo:

import math

def calculando (x):
    return x*math.pi

"""


    
