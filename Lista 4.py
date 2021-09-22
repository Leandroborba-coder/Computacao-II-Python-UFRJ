#Questão 1: Para cada item abaixo, realize as seguintes tarefas:

    #Dê uma breve explicação sobre que tipos de situação geram a exceção considerada. Coloque essa explicação como comentário (#) no início do primeiro campo de código.
    #Dê um exemplo de um trecho de código que possa gerar a exceção considerada. Escreva seu exemplo de código no primeiro campo de código.
    #Descreva uma situação concreta em que o seu exemplo de código efetivamente irá gerar a exceção. Coloque essa descrição como um segundo bloco de comentário (#) no final do primeiro campo de código, abaixo do seu exemplo de código.
    #Finalmente, no segundo campo de código, reescreva o seu exemplo de código fazendo o tratamento de exceções com os comandos try etc.
    #a) IndexError

       # A exceção IndexError ocorre quando acontecem erros de indexação em listas, tuplas e strings. Veja o exemplo abaixo:

        # lista = [1,5,7,8,4,9,4,8]
        # lista[10]
        # IndexError

        # Ao selecionar o indice 10 na lista "lista", ocorrerá um erro, pois a lista "lista" possui indices de 0 a 7, sendo o indice 0 o primeiro elemento e o
        # indice 7 o ultimo elemento.

        # Considerando a possibilidade de que o usuário de um programa Python possa cometer esse erro, é interessante o programador escrever linhas de código para
        # fazer o tratamento adequadro desta exceção.

        # Ao criar uma classe para realizar o tratamento desta exceção, o programa não será fechado, como normalmente ocorria com os códigos anteorimente feitos por nós,
        # mas sim exibirá uma mensagem indicando as restrições de indexação de um lista ou tupla ou string e retornará novamente ao usuário que ele insira novamente 
        # um dado que seja aceito pelo programa.

            while(True):
              try:
                lista = eval(input("Digite uma lista:"))
                indice = int(input("Digite um indice:"))
                resultado = lista[indice]
                break
              except IndexError:
                indice_max = len(lista) -1
                print("Os indices válidos são de 0 a",indice_max)
                
            print(resultado)

    #b) KeyError

        #O erro KeyError ocorre quando as chaves em dicionários são usadas de maneira incorreta. Vejo o exemplo abaixo relacionando o nome das pessoas com suas respectivas idades:

        # pessoas = {'Leandro':21, 'Luiz':30, 'Victor': 19}
        # pessoas['Carlos']
        # KeyError

        #No exemplo acima podemos perceber que, ao inserir uma nome que não está presente no dicionário "pessoas", é gerado um erro do tipo KeyError.

        while(True):
          try:
            pessoas = {'Leandro':21, 'Luiz':30, 'Victor': 19}
            consulta = input("Digite um nome para consultar a idade desta pessoa:")
            resultado = pessoas[consulta]
            break
          except KeyError:
            print(consulta,"não está presente no dicionário do sistema. Por gentileza, faça uma nova consulta.")
            
        print(resultado)

    #c)NameError
        #O erro NameError ocorre quando o usuário tenta acessar uma variável que nunca foi declarada ou nunca foi atribuído nenhum valor. Veja o exemplo abaixo:

        #frases = "O céu é azul, a rosa é a vermelha"
        #print(fresas)
        #NameError

        #Como podemos perceber, o programador digitou a palavra 'frase' de maneira errada no comando print e, como a variável 'fresas' nunca foi declarada e nunca recebeu nenhum valor, ocorrerá um erro do tipo NameError

        def Mensagembonita():
          '''Chame a função Mensagembonita para ler a mensagem bonita do dia'''

          try:
            frases = "O céu é azul, a rosa é a vermelha"

            print(fresas)
          
          except NameError:
            print("Existe uma variável não definida. Reveja seu código")

        Mensagembonita()

    #d)TypeError
        #O error TypeError ocorre quando usamos um tipo de dado incompatível com a operação da função. Veja o exemplo abaixo:

        # divisao('4','2')
        # resultado = x/y
        # print(resultado)
        # TypeError

        #Como podemos perceber, a função 'divisao' realiza a divisão do número x pelo y. Para realizar uma operação de divisão, só é possível admitir dados do tipo int e/ou float.
        #No exemplo acima, o usuário iseriu dois dados do tipo string. Em virtude do usuário ter inserido um dado de TIPO incompatível com a operação da função, ocorreu o erro do tipo TypeError

        def divisao(x,y):
          try:
            resultado = x/y
            print(resultado)

          except TypeError:
            print("Só é possível inserir valores do tipo int e/ou float. Outros tipos de dados não são suportados")

        divisao('4','2')
        divisao(4,2)

    #e) ValueError

        #O error ValueError ocorre quando um valor inserido pelo usuário não é apropriado para realizar uma determinada tarefa. Veja o código abaixo:

        # animais = ('Gato','Cachorro','Tartaruga','Cavalo','Pássaro','Macaco','Onça')
        # consulta = int(input("Digite um número de 0 a 6 para saber qual animal você seria em outra vida:"))
        #consulta = 'gato'
        # print(animais[consulta])

        #Como podemos perceber no código acima, o usuário inseriu uma string escrito 'gato'. Entretanto, a variável 'consulta' admite apenas números inteiros, já que ela está sendo utilizada como indice de uma lista 'animais'.
        # Por essa razão, ocorre o error do tipo ValueError.

        while(True):
          try:
            animais = ('Gato','Cachorro','Tartaruga','Cavalo','Pássaro','Macaco','Onça')
            consulta = int(input("Digite um número de 0 a 6 para saber qual animal você seria em outra vida:"))

            print(animais[consulta])

            break
          
          except ValueError:
            print("Você só pode digitar números!") 

    #f) ZeroDivisionError
        #O erro ZeroDivisionError ocorre quando o usuário tenta dividir um número por zero. Este erro ocorre também para as operações de módulo (%) e de obter a parte inteira (//). Veja o exemplo abaixo:

        # numerador = 4
        # denominador = 0
        # resultado = numerador/denominador
        # print(resultado)
        # ZeroDivisionError

        #Ocorreu um erro no exemplo do código acima pois o usuário tentou dividir o número 4 por 0, o que gerou um erro do tipo ZeroDivisionError.

        while (True):
          try:
            print("Seja bem-vindo a calculadora de divisão.")
            numerador = int(input("Insira um número inteiro para o numerador:"))
            denominador = int(input("Insira um número inteiro para o denominador:"))

            resultado = numerador/denominador
            print("O resultado da divisão de",numerador, "pelo número", denominador, "é:", resultado)

            break
          except ZeroDivisionError:
            print("Você dividiu um número por zero. Insira números diferentes de zero.")
            

#Questão 2: Identifique e faça o tratamento, através do uso dos comandos try etc., das exceções que podem acontecer durante a execução do código abaixo. A identificação das exceções pode ser feita em um comentário no início do campo de código e o tratamento pode ser feito editando-se o próprio código apresentado.

# (Identificacao das possiveis excecoes), 
# Se o usuário inserir zero, será gerado um erro: ZeroDivisionError
# O usuário não pode inserior valores não inteiros e/ou menores do que zero. 
# O usuário pode inserir uma nome errado no campo da quantidade de parcelas (NameError)
# O usuário pode inserir um tipo de dado incompatível com a função (TypeError)
       
class Negativo(Exception):
  pass

while (True):
  try:
    print("Este programa calcula a media geometrica de uma sequencia de parcelas (numeros reais)")
    n = eval(input("Entre com um numero inteiro, representando a quantidade de parcelas:"))

    if n < 0 or n != round(n):
      raise Negativo
     
    i = 0
    prod = 1
    while (i < n):
      p = eval(input("Entre com uma parcela"))
      prod = prod * p
      i = i + 1
    media = prod ** (1.0 / n) #raiz n-esima de prod
    break

  except ZeroDivisionError:
    print("Não é possível inserir um número de parcelas igual a zero.Insira apenas valores inteiros e maiores do que zero. (ZeroDivisionError)")

  except Negativo:
    print("Não é possível inserir valores MENORES DO QUE ZERO ou valores NÃO INTEIROS no número de parcela. Insira apenas valores inteiros e maiores do que zero")

  except NameError:
    print("Só é possível inserir números no campo da quantidade de parcelas. (NameError)")

  except TypeError:
    print("Só é possível inserir números no campo da quantidade de parcelas. (TypeError)")

#Questão 3: Modifique o código do programa abaixo (edite o próprio código apresentado) para que ele dispare uma exceção NotaInvalida se o usuário informar uma nota que não seja um número maior ou igual a zero e menor ou igual a dez e uma exceção CreditoInvalido se o usuário informar uma quantidade de créditos que não seja um número inteiro maior do que zero.

class NotaInvalida(Exception):
  pass
class CreditoInvalido(Exception):
  pass

print("Este programa calcula o CR do aluno.")
n = 0
c = 1
while (n != c):
  try:
    N = eval(input("Entre com uma lista das notas do aluno:"))

    for g in N:
      if  g > 10 or g < 0:
        raise NotaInvalida


    n = len(N)
    C = eval(input("Entre com as respectivas quantidades de creditos de cada disciplina do aluno:"))

    for h in C:
      if h <= 0 or h != round(h):
        raise CreditoInvalido

    c = len(C)

  except NotaInvalida:
    print("Só é possível inserir valores maiores ou iguais a zero e menores ou iguais a 10 para as notas")

  except CreditoInvalido:
    print("Só é possível inserir valores inteiros e maiores do que zero.")

i = 0
soma = 0
cred = 0
while (i < n):
  soma = soma + C[i] * N[i]
  cred = cred + C[i]
  i = i + 1
cr = soma / cred


