#  Programa que calcule quantos dias completos são 705 horas. 
# E quantas horas sobram?

hours = 705

dias = hours // 24
print("705 horas = " + str(dias)+ " dias.")

hours_left = hours % 24
print("E sobram " + str(hours_left)+" horas.")