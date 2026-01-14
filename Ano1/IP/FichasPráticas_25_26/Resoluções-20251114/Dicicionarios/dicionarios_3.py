# dicionarios
a={'one':'uno','two':'dos','three':'tres'}
print(a)

k = a.keys()
print(k)
a['four']= 4
print(a)
print(k)

input('     Enter para continuar 1')

del a['two']
print(a)

input('     Enter para continuar 2')

print(iter(a))
