try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# except: # Aqui quando o programa der um erro ele irá mostrar essa menssagem
#     print('Infelizmente tivemos um problema!')
#
# # Também posso fazer assim:
#
# except Exception as erro:
#     print(f'o problema encontrado foi: {erro.__class__}') # aqui ele irá falar o nome da classe do erro

# Também posso colocar vários atributos no "except":

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel dividir um númeor por 0')

except KeyboardInterrupt:
    print('O usuário não preferiu informar os dados!')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')


else:
    print(f'O resultado foi: {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')