#Questão 1: Construa uma classe MatrizQuadrada para representar matrizes quadradas  n×n . Esta classe deve conter os atributos e métodos listados a seguir:

    #Atributo tamanho, que contém o número de linhas e colunas da matriz (que será sempre quadrada);
    #Atributo mat, que contém os valores da matriz, armazenados na forma de uma lista de listas;
    #Método __init__(self,tamanho,mat) para inicializar os atributos de um objeto da classe;
    #Método SomaLocal(self,M2) para realizar a soma da matriz armazenada no objeto de onde se está chamando o método (objeto local) com a matriz do objeto M2 e armazenar o resultado no objeto local;
    #Método SomaNovo(self,M2) para realizar a soma da matriz armazenada no objeto de onde se está chamando o método (objeto local) com a matriz do objeto M2, criar um novo objeto da classe MatrizQuadrada e armazenar o resultado neste novo objeto;
    #Vamos reforçar a diferença entre os dois métodos de soma. Ao somarmos dois objetos M1 e M2 com SomaLocal, o resultado é armazenado no próprio objeto M1, ou seja, esse objeto terá seu valor alterado do que possuía antes para o valor resultante da soma. Já ao somarmos M1e M2 com SomaNovo, nenhum dos objetos terá seu valor alterado. O valor da soma será armazenado em um terceiro objeto, que deverá ser criado e retornado pelo método.
    #Método Imprime(self) para imprimir no console, na notação em que costumamos escrever matrizes, e não na notação de lista de listas, a matriz armazenada no objeto.
    #Observação: Os métodos SomaLocal(self,M2) e SomaNovo(self,M2) devem verificar se as matrizes armazenadas no objeto local e em M2 possuem a mesma dimensão. Caso contrário, a soma não pode ser feita e uma mensagem de erro deve ser impressa no console.

class MatrizQuadrada():
  def __init__(self,tamanho,mat):
    if tamanho[0] != tamanho[1]:
      return ("Essa matriz não é quadrada! Só é possível inserir matriz N x N")
    self.tamanho = tamanho
    self.mat = mat

  def SomaLocal(self,M2):
    self.M2 = M2
    soma = []
    for i in range(len(self.mat)):   
        soma.append([])
        for j in range(len(self.mat[0])):
            soma[i].append(self.mat[i][j] + M2.mat[i][j])

    self.mat = soma
      
  def SomaNovo(self,M2):    
    soma = []
    for i in range(len(self.mat)):   
        soma.append([])
        for j in range(len(self.mat[0])):
            soma[i].append(self.mat[i][j] + M2.mat[i][j])

    m3 = MatrizQuadrada(self.tamanho,soma)
    return m3
      
  def Imprime(self):
    for i in self.mat:
        print(i)

#Questão 2: Suponha que o Python não possua um tipo de dados e métodos específicos para descrever conjuntos e construa uma classe Conjunto para representar conjuntos. Esta classe deve conter os atributos e métodos listados a seguir:

    #Atributo conj, que contém uma lista dos elementos do conjunto. Seguindo a definição matemática de conjuntos, esta lista nunca deve conter elementos repetidos;
    #O Método Mágico de inicialização dos atributos de um objeto da classe;
    #Métodos Mágicos para que os operadores +, -, * e / da linguagem do Python possam ser utilizados com objetos da classe Conjunto para realizarem as seguintes operações, respectivamente: união de conjuntos, diferença de conjuntos, produto cartesiano de conjuntos e interseção de conjuntos;
    #Um Método Mágico para que o conjunto possa ser exibido no console da maneira usual, como uma lista de elementos entre chaves e separados por vírgula.
    #Observação: O tipo de dados do Python que descreve conjuntos não deve ser usado em lugar nenhum do seu código, assim como os métodos específicos do Python de manipulação de conjuntos. Para os propósitos desta questão, é como se eles não existissem e você estivesse implementando conjuntos do zero.

class Conjunto():
  conj=[]
  def __init__(self,conjunto):
    self.conj = conjunto

  def __add__(self,conj2):
    nConj = []
    for i in self.conj:
      nConj.append(i)

    for i in conj2.conj:
      if i not in nConj:
        nConj.append(i)
    CJ= Conjunto(nConj)

    return CJ

  def __sub__(self,conj2):
    nConj= []

    for i in self.conj:
      if i not in conj2.conj:
        nConj.append(i)
      CJ=Conjunto(nConj)

    return CJ

  def __mul__(self,conj2):
    nConj=[]

    for i in self.conj:
      for j in conj2.conj:
        nConj.append((i,j))
        CJ= Conjunto(nConj)

    return CJ

  def __truediv__(self, conj2):
    nConj =[]

    for i in self.conj:
      if i in conj2.conj:
        nConj.append(i)
      CJ=Conjunto(nConj)

    return CJ

  def __str__(self):
    conjStr= '{'+ str(self.conj) +'}'

    return conjStr

#Questão 3: Suponha que o Python não possua um tipo de dados e métodos específicos para descrever números complexos e construa uma classe NumComplexo para representar números complexos. Esta classe deve conter os atributos e métodos listados a seguir:

    #Atributo real, que contém a parte real do número complexo;
    #Atributo imag, que contém a parte imaginária do número complexo;
    #O Método Mágico de inicialização dos atributos de um objeto da classe;
    #Métodos Mágicos para que os operadores +, - e * da linguagem do Python possam ser utilizados com objetos da classe NumComplexo para realizarem as seguintes operações, respectivamente: soma, diferença e produto de números complexos;
    #Um Método Mágico para que o número complexo possa ser exibido no console da maneira usual;
    #Observação: O tipo de dados do Python que descreve números complexos não deve ser usado em lugar nenhum do seu código, assim como os métodos específicos do Python de manipulação de números complexos. Para os propósitos desta questão, é como se eles não existissem e você estivesse implementando números complexos do zero.

class NumComplexo():
  real=0.0
  imag=0.0 
  def __init__(self,real,imag):
    self.real = real
    self.imag = imag
 
  def __add__(self,v2):
    novoReal = self.real + v2.real
    novoImag = self.imag + v2.imag
    num = NumComplexo(novoReal,novoImag)
    return num 

  def __sub__(self,v2):
    novoReal = self.real - v2.real
    novoImag = self.imag - v2.imag
    num= NumComplexo(novoReal,novoImag)
    return num

  def __mul__ (self,v2):
    novoReal = self.real * v2.real + ((self.imag * v2.imag)*(-1))
    novoImag = self.real * v2.imag + self.imag * v2.real
    num= NumComplexo(novoReal,novoImag)
    return num
  
  def __str__(self):
    if self.imag >=0:
      numStr = str(self.real) + '+' + str(self.imag) + 'j'
      return numStr 
      
    else:
      numStr = str(self.real)  + str(self.imag) + 'j'
      return numStr

#Questão 4: Construa uma classe Pessoa, uma classe Homem, uma classe Mulher e uma classe Casal de acordo com as seguintes instruções:

    #As classes Homem e Mulher devem ser subclasses da classe Pessoa;
    #A classe Pessoa deve possuir um atributo nome, um atributo idade e um atributo cpf;
    #A classe Homem deve possuir um atributo booleano barba, indicando se ele possui ou não barba;
    #A classe Mulher deve possuir um atributo booleano gravida, indicando se ela está ou não grávida no momento;
    #A classe Casal deve possuir dois atributos, membro1 e membro2, que são objetos da classe Pessoa, informando os componentes do casal;
    #As quatro classes devem possuir Métodos Mágicos de inicialização dos atributos de um objeto da classe;
    #As quatro classes devem possuir Métodos Mágicos para que as informações do objeto sejam exibidas de maneira organizada no console;
    #A classe Pessoa deve possuir o Método Mágico para que o operador + da linguagem do Python possa ser utilizado com objetos dessa classe para construir um objeto da classe Casal.

class Pessoa(object):
  def __init__(self,nome,idade,cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

  def __str__(self):
      return 'Abaixo estão os dados referentes a este pessoa: \nNome: %s \nIdade: %s \nCPF: %s'% (self.nome,self.idade,self.cpf)

class Homem(Pessoa):
  def __init__(self,nome,idade,cpf,barba):
    self.barba = barba
    Pessoa.__init__(self,nome,idade,cpf)

  def __str__(self):
    if self.barba == True:
      return 'Abaixo estão os dados referentes a este homem: \nNome: %s \nIdade: %s \nCPF: %s \nBarba: Sim'% (self.nome,self.idade,self.cpf)
    else:
      return 'Abaixo estão os dados referentes a este homem: \nNome: %s \nIdade: %s \nCPF: %s \nBarba: Não'% (self.nome,self.idade,self.cpf)

class Mulher(Pessoa):
  def __init__(self,nome,idade,cpf,gravida):
    self.gravida = gravida
    Pessoa.__init__(self,nome,idade,cpf)
    
  def __str__(self):
    if self.gravida == True:
      return 'Abaixo estão os dados referentes a esta mulher: \nNome: %s \nIdade: %s \nCPF: %s \nGrávida: Sim\n'% (self.nome,self.idade,self.cpf)
    else:
      return 'Abaixo estão os dados referentes a esta mulher: \nNome: %s \nIdade: %s \nCPF: %s \nGrávida: Não\n'% (self.nome,self.idade,self.cpf)

class Casal(Homem,Mulher):
  def __init__(self, membro1, membro2):
    self.membro1 = membro1
    self.membro2 = membro2

  def __str__(self):
    return f'Abaixo estão as informações do casal: \n\n{self.membro1} \n\n\n{self.membro2}'

#Questão 5: Construa uma classe Pilha para representar a estrutura de dados conhecida como pilha. Esta estrutura de dados funciona exatamente como uma pilha de pratos: um novo prato é sempre adicionado no topo da pilha e, ao retirar um prato, o prato retirado é sempre aquele que estava no topo da pilha. Isto é, as operações de inserção e remoção em uma pilha sempre acontecem em seu topo. A classe Pilha deve conter os atributos e métodos listados a seguir:
    #Atributo elementos, que contém os elementos armazenados na pilha, na forma de uma lista. O topo da pilha será sempre o primeiro elemento da lista (o elemento com índice 0);
    #O Método Mágico de inicialização dos atributos de um objeto da classe;
    #Um Método Mágico para que a pilha possa ser exibida no console em um formato amigável, sem os colchetes utilizados nas listas;
    #Método Empilha(self,e) para empilhar um novo elemento e no topo da pilha;
    #Método Desempilha(self) para desempilhar o elemento que está no topo da pilha e retornar esse elemento.
    #Observação: No método Desempilha, se a pilha já estiver vazia, o método deve imprimir uma mensagem de erro e retornar o número zero.

class Pilha():
  def __init__(self,elementos):
    self.elementos = elementos

  def Empilha(self,e):
    self.e = e
    self.elementos.insert(0,self.e)

  def Desempilha(self):
    if len(self.elementos) == 0:
      print ("Erro! A pilha já está vazia!")
      return 0

    return self.elementos.pop(0)

  def __str__(self):
     resultado = ''
     for i in self.elementos:
         resultado += i
         resultado += '\n'
     return resultado

