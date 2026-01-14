#
# POP Setembro 2023
#
# IP Ficha 02  Exercicio 01
#
#   	Escreva um programa que coloque no ecrã uma árvore com o seguinte formato:
#      *
#    * * *
#   * * * * *
#    / | \
#      |
#


# Opção 1
print('               Opcão 1:')
print('      *')
print('    * * *')
print('   * * * * ')
# A single backslash (\) within a string literal represents an escape character.
# Use the syntax "\\" within the string literal to represent a single backslash.
print('    / | \\')   # duplo backslash
print('      |')
print()  # linha em branco



# Opção 2
print('               Opcão 2:')
l1= '      *'
l2= '    * * *'
l3= '   * * * * '
l4= '    / | \\'
l5= '      |'
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print()  # linha em branco




# Opção 3
print('               Opcão 3:')
l1= '      *'
l2= '    * * *'
l3= '   * * * * '
l4= '    / | \\'
l5= '      |'
print(l1+'\n'+l2+'\n'+l3+'\n'+l4+'\n'+l5+'\n')
# \n  causa mudança de linha




# Opção 4
print('               Opcão 4:')
# Use raw string:  syntax r"\" to treat backslash (\) as a literal character, and not as an escape character.
l4= r"    / | \ "
print(l1+'\n'+l2+'\n'+l3+'\n'+l4+'\n'+l5+'\n')



# Opção 5
print('               Opcão 5:')
l1= '      *\n'
l2= '    * * *\n'
l3= '   * * * * \n'
l4= '    / | \\ \n'
l5= '      |\n'
print(l1+l2+l3+l4+l5)


# Opção 6
print('               Opcão 6:')
print('      *\n    * * *\n   * * * * \n    / | \\ \n      |\n')