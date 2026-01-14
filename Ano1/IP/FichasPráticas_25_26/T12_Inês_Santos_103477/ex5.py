# Desenvolva uma aplicação que simule uma TV criando-a como um objeto. O utilizador
# deverá ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de
# faixas válidas ([0; 99] e [0; 30], respetivamente).

class TV:
    def __init__(self, num_canal = 0, num_volume = 0):
        if 0 <= num_canal <= 99:
            self.canal = num_canal
        else: 
            self.canal = 0
        
        if 0 <= num_volume <= 30:
            self.volume = num_volume
        else: 
            self.volume = 0
    
    def mostrarCanal(self):
        print(self.canal)
    
    def mudarCanal(self, new_canal):
        if 0 <= new_canal <= 99:
            self.canal = new_canal
    
    def aumentarVolume(self):
        if 0 <= self.volume < 30:
            self.volume += 1
        else:
            print("Volume máximo atingido.")

    def diminuirVolume(self):
        if self.volume > 0 and self.volume <= 30:
            self.volume -= 1
        else:
            print("Não é possível diminuir mais o volume da TV.")

# criar objeto TV
tv = TV(1) # apenas atribui nº do canal (canal 1)

tv.mostrarCanal()
tv.mudarCanal(22)
tv.mostrarCanal()

tv.aumentarVolume()
tv.diminuirVolume()
tv.diminuirVolume()

tv.aumentarVolume()
tv.aumentarVolume()
tv.aumentarVolume()

print(f"Nº do Canal Atual: {tv.canal}\n Volume atual: {tv.volume}")
