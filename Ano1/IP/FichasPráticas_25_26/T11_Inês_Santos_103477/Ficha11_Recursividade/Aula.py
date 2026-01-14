def countdown(n):
    if n <= 0:
        print('Boom!')
    else:
        print('Antes: ',n)
        countdown(n-1)
        print('- Depois: ',end='')
        print(n)

countdown(4)


