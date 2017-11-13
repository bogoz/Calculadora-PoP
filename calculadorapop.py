# Calculadora Linha De Comando
# Autor: Washington Ferreira Prata (BoGoZ).
# Brasilia, 30 De Outubro De 2017.


import sys
import re


def impressao_menu_help():
    print()
    print('------------------------------------ [ Calculadora PoP 1.0 ] ------------------------------------')
    print()
    print('Autor: Washington Ferreira Prata (BoGoZ) | GitHub: https://github.com/bogoz')
    print()
    print('--------------------------------------------- [ HELP ] ----------------------------------------------')
    print()
    print('COMANDOS: [ \'Operador\' \'Sinal\' \'Operando\' ]')
    print()
    print('SINAIS: [ Soma=\'+\' Subtração=\'-\' Multiplicação=\'*\' Divisão=\'/\' Porcentagem=\'%\' Juros Compostos=\'%%\' ]')
    print()
    print('EXEMPLO SIMPLES: python calculadorapop.py 2 + 2')
    print()
    print('EXEMPLO JUROS COMPOSTO: python calculadorapop.py 2 %% 4 * 10 \nSIGNIFICADO: Valor Base=\'2\' Juros=\'4\' Quantidade De Vezes=\'10\'')
    print()
    print('--------------------------------------------- [ HELP ] ----------------------------------------------')
    print()


comandos_sistema = sys.argv

try:
    operador = comandos_sistema[1]
    sinal = comandos_sistema[2]
    operando = comandos_sistema[3]

except:
    impressao_menu_help()
    quit()


try:
    vezes = comandos_sistema[5]
    impressao_modo = 'Modo Juros Compostos'

except:
    impressao_modo = 'Modo Calculadora Simples'


impressao_menu_help()


#FUNÇÕES
def soma(numero_1, numero_2):
    return float(numero_1) + float(numero_2)

def subtracao(numero_1, numero_2):
    return float(numero_1) - float(numero_2)

def multiplacao(numero_1, numero_2):
    return float(numero_1) * float(numero_2)

def divisao(numero_1, numero_2):
    return float(numero_1) / float(numero_2)

def modulo(numero_1, numero_2):
    return int(numero_1) % int(numero_2)

def porcentagem(numero_1, numero_2):
    return float(numero_1) * float(numero_2) / 100

def juros_compostos(numero_1 , numero_2 , quantidade):

    contador = 0
    juros = float(numero_1)

    while contador < int(quantidade):
        juros += juros * float(numero_2) / 100
        contador += 1

    return juros


#ESTRUTURA DE DECIÇÕES
if sinal == '+':
    resultado = soma(operador , operando)

elif sinal == '-':
    resultado = subtracao(operador , operando)

elif sinal == '*':
    resultado = multiplacao(operador , operando)

elif sinal == '/':
    resultado = divisao(operador , operando)
    resto = modulo(operador , operando)

elif sinal == '%':
    resultado = porcentagem(operador , operando)

elif sinal == '%%':
    resultado = juros_compostos(operador , operando , vezes)

else:
    sinal = 'sinal erro';


# IMPRESSÃO DO RESULTADO

print(impressao_modo)
print()

if sinal == '/':
    print('Total: ' , int(resultado))
    print('Resto: ' , resto)

elif sinal == '%':
    print('Total: ' , resultado)
    print('Soma Total: ' , float(operador) + resultado)
    print('Subtração Total: ' , float(operador) - resultado)

elif sinal == '%%':
    numero_fracionado = re.findall(r'.+\...' , str(resultado))
    resultado =  float(numero_fracionado[0]) + 0.01
    print('Total: ' , resultado)

elif sinal == 'sinal erro':
    print('!Sinal Incorreto!')

else:
    numero_fracionado = re.findall(r'\..+' , str(resultado))

    if numero_fracionado[0] == '.0':
        print('Total: ' , int(resultado))

    else:
        print('Total: ' , resultado)
