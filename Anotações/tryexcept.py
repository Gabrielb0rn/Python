# Divisão numérica

try:
    
    numeroUm = int(input('Digite o primeiro número: '))
    numeroDois = int(input('Digite o segundo número: '))

    resultado = numeroUm / numeroDois
    print(f'Resultado: {resultado}')
    
except ZeroDivisionError:
    
    print('Não é possível dividir um número por zero!')
    
except ValueError:
    
    print('O valor digitado não é numérico!')
    
    
# except (ZeroDivisionError, ValueError):
    
#     print('Dados não aceitos! :(')
