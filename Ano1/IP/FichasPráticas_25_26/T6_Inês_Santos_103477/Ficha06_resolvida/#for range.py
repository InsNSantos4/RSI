# Exemplos de Ciclos for variavel_iteração in range numérico


print( '\nComando: for i in range(10)')
input('.....Press Enter to Start')
for i in range(10):
    print(i)


print()
print( 'Próximo comando: for i in range(-5,2)')
input('.....Press Enter to Continue')
for i in range(-5,2):
    print(i)


print()
print( 'Próximo comando: for i in range(5,20,3)')
input('.....Press Enter to Continue')
for i in range(5,20,3):
    print(i)


print()
print( 'Próximo comando: for i in range(7,0)  como 0 é menor que 7, termina imediatamente')
input('.....Press Enter to Continue')
for i in range(7,0):
    print(i)


print()
print( 'Próximo comando: for i in range(7,0,-1)')
input('.....Press Enter to Continue')
for i in range(7,0,-1):
    print(i)


print()
print( 'Próximo comando: for i in (7,-1,8) se "esquecermos" de colocar o "range", vai iterar o tuplo (7,-1,8) e não um range')
input('.....Press Enter to Continue')
for i in (7,-1,8):
    print(i)