import math


#A função deve ser definida no código
def funcao1(x): #como exemplo, a função x^2 + 2x + 3
    return pow(x, 2) + 2 * x + 3 + pow(x,3)

def funcao2(x): # como exemplo, a função x^2 - 1
    return pow(x,2) - 1


###
# Para usar a função, basta chamar a função raizes_no_intervalo(funcao, pontoa, pontob, iteracoes,erro)
# Onde:
# funcao é a função que se deseja encontrar a raiz
# pontoa e pontob são os pontos que delimitam o intervalo onde se deseja encontrar a raiz
# iteracoes é a quantidade de pontos que serão colocados INICIALMENTE para encontrar as raizes
# erro é o erro maximo aceitavel para a raiz
# Exemplo:
# bisseccao(funcao1, -30, 30, 50, 0.0001)

def linspace(ini,fim,n):
    step = (fim-ini) / (n - 1)#calcula o tamanho do passo baseado na quantidade de passos entre dois numeros
    return [ini + step * i for i in range(n)]

def truncar_casas_decimais(n, ncasas): #trunca um numero.
    fator = ncasas ** 10
    return math.trunc(fator * n) / fator

def encontra_raiz(funcao, pontoA, pontoB, iteracoes):
    x = linspace(pontoA,pontoB, iteracoes)
    y = []
    raizes = []
    for element in x:
        y.append(funcao(element))

    for i in range(len(y) - 1):
        if y[i] < 0 < y[i + 1] or y[i] > 0 > y[i + 1]:
            raizes.append((x[i], x[i+1]))
    return raizes

def bisseccao_aux(funcao, a,b,erro):
    while (abs(b - a) > erro) or (abs(funcao((a + b) / 2)) > erro):
        x = (a+b)/2
        fx = funcao(x)
        if ((fx * funcao(a)) < 0):
            b = x
        elif((fx*funcao(b)) < 0):
            a = x
        resultado = fx
    raiz = [x, resultado]
    return raiz


def bisseccao(funcao, pontoa, pontob, iteracoes,erro): #As iteracoes são a quantidade de pontos colocados para achar a raiz inicialmente, valores maiores geram um numero inicial mais proximo
    x = encontra_raiz(funcao, pontoa, pontob, iteracoes)
    print("Foram encontradas {} raizes:".format(len(x)))
    print("Com erro = {}".format(erro))
    for element in x:
        raiz = bisseccao_aux(funcao, element[0], element[1], erro)
        print("\nRaiz encontrada = {}".format(raiz[0]))
        print("Para o f(x) = {}".format(raiz[1]))
    return 0






bisseccao(funcao2, -30, 30, 50, 0.0001)