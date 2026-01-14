# Este programa soma horas:
#    hh1 mm1 ss1  +  hh2 mm2 ss2

print("""Este programa soma horas  (h m s)
 hh1 mm1 ss1  +  hh2 mm2 ss2\n""""")

hh1=int(input("Introduza hh1: "))
mm1=int(input("Introduza mm1: "))
ss1=int(input("Introduza ss1: "))
print()
hh2=int(input("Introduza hh2: "))
mm2=int(input("Introduza mm2: "))
ss2=int(input("Introduza ss2: "))

#Soma dos segundos
ss_aux = ss1 + ss2
ss = ss_aux % 60       # obter os segundos de 0s - 59s
mm_s = ss_aux // 60  # obter minutos completos resultante da soma dos segundos

# Soma dos minutos
mm_aux = mm1 + mm2 + mm_s # soma dos minutos introduzidos e dos minutos vindos da soma dos segundos
mm = mm_aux % 60  # obter os minutos de 0s - 59s
hh_m = mm_aux // 60  # obter horas completas resultante da soma dos minutos

# Soma das horas
hh = hh1 + hh2 + hh_m # soma das horas introduzidas e das horas vindos da soma dos minutos

print(f"Soma = {hh}h {mm}m {ss}s")