
import time

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print('Número inválido')


print('Escolha uma operação') , time.sleep(1)
op = input('Soma(S), Subtração(SU), Divisão(D), Multiplicação(M): ').upper()

while not op in ['S', 'SU', 'D', 'M']:
    print('Operação inválida')
    print('Escolha uma operação') , time.sleep(1)
    op = input('Soma(S), Subtração(SU), Divisão(D), Multiplicação(M): ').upper()

if op == 'S':
    resu = n1 + n2

elif op == 'SU':
    resu = n1 - n2

elif op == 'D':
    resu = n1 / n2

elif op == 'M':
    resu = n1 * n2

print(f'O resultado da operação é {resu}')

if resu.is_integer():
    print('Este número é inteiro,', end=' ')
    if resu % 2 == 1:
        print('ímpar,', end=' ')
    else:
        print('par,', end=' ')
else:
    print('Este número é decimal, não se classifica como par ou impar', end=' ')

if resu >= 0:
    print('e é positivo')
else:
    print('e é negativo')




