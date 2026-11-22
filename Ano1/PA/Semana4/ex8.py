a=1
b=1
print(a is b)

a=[1]
b=[1]
print(a is b)

a=[1]
b=a
print(a is b)

a=[1]
b=a+[] #ou b=a[:]
print(a is b)