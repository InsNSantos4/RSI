#from datetime import datetime
from datetime import date
from ex1 import Pessoa
import tkinter as tk

class LabelAtributo(tk.Frame):
    def __init__(self, parent, title, text):
        super().__init__(parent)
        self.lable_title = tk.Label(self, text=title)
        self.lable_text = tk.Label(self, text=text)

        self.lable_title.pack(side=tk.LEFT) #Alinhado à esquerda do anterior (parent)
        self.lable_text.pack(side=tk.LEFT) #Alinhado à esquerda do anterior (entry)


def show_person(person : Pessoa):
    mostra_pessoa = tk.Tk()     # cria objeto do tipo Janela gráfica
    mostra_pessoa.geometry("350x200")
    mostra_pessoa.title("Pessoa")
    

    # Para aparecer Pop-up:
    #tk.messagebox.showinfo("Pessoa:", person) 

    first_name = LabelAtributo(mostra_pessoa,"Primeiro Nome:", person.first_name)
    last_name = LabelAtributo(mostra_pessoa,"Último Nome:", person.last_name )
    birthday = LabelAtributo(mostra_pessoa,"Data de Nascimento:", person.birthdate)
    address = LabelAtributo(mostra_pessoa,"Morada:", person.address)
    height = LabelAtributo(mostra_pessoa,"Altura:", person.height)


    # first_name = tk.Label(mostra_pessoa, text=p)
    #first_name_title = tk.Label(mostra_pessoa, text=)
    # last_name = tk.Label(mostra_pessoa, text=person.last_name)
    # birthday = tk.Label(mostra_pessoa, text=person.birthdate)
    # address = tk.Label(mostra_pessoa, text=person.address)
    # height = tk.Label(mostra_pessoa, text=person.height)

    # Criar botão:
    #b = tk.Button(mostra_pessoa, text="Pessoa")
    #b.pack()                    # o pack renderiza por ordem
    #first_name_title.pack(side='left')
    #first_name.pack(side='left')
    first_name.pack()
    last_name.pack()
    birthday.pack()
    address.pack()
    height.pack()

    mostra_pessoa.mainloop()    # ciclo infinito da janela (programa, depois de executado, só acaba quando eu clicar na cruz para fechar)


#código de teste do Pessoa_window.py:
if __name__ == "__main__":
    
    pessoa_1 = Pessoa("Rui", "Oliveira", date(2000, 5, 17), "Rua 25 abril", 1.90)
    show_person(pessoa_1)