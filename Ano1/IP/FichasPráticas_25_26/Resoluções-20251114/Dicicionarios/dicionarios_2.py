
a={'one':'uno','two':'dos','three':'tres'}
print(a)


input('     Enter para continuar 1')
k = list(a)
print(k)


d=a.keys()
print(d)
print(list(d))

input('     Enter para continuar 2')
vals = a.values()
print(vals)

input('     Enter para continuar 3')
vals=list(vals)
print(vals)
for i in vals:
    print(i)

input('     Enter para continuar 4')
for i in range(len(vals)):
    print(vals[i])

