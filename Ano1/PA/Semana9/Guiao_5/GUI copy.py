from Guiao_5 import Pessoa
from datetime import datetime


import tkinter as tk
from tkinter import messagebox

import json

class Frame_Atributo():
    
    def __init__(self, parent, atributo : str, valor ):
        
        self.frame = tk.Frame(parent)

        self.label_atributo = tk.Label(self.frame, text= atributo)
        self.label_valor = tk.Label(self.frame, text= valor)

        self.entry = tk.Entry(self.frame)

        self.edit_mode = False                      #Flag

        self.label_atributo.pack(side=tk.LEFT)
        self.label_valor.pack(side=tk.LEFT)

    def toggle(self):               # Flag swap
        if self.edit_mode:
            
            self.entry.pack_forget()
            self.label_valor.config(text=self.entry.get())
            self.label_valor.pack()
        else:

            self.label_valor.pack_forget()
            self.entry.pack()

        self.edit_mode = not self.edit_mode     #Deixa de ser o que quer que esteja, trocamos a flag

    def get_valor(self):                    #Conseguir os valores para usar depois
        if self.edit_mode:
            return self.entry.get()
        else:
            self.label_valor.cget("text")

    def pack(self):                     # Tenho que adicionar uma função pack porque a classe tem um frame mas não é um frame
        self.frame.pack(anchor="w", pady=2)



def mostrar_pessoa(pessoa : Pessoa):
    

    janela_pessoa = tk.Tk()
    janela_pessoa.geometry("600x400")
    janela_pessoa.title(f"Dados de {pessoa.primeiro_nome} {pessoa.apelido}")



    #               Atributos do Object

    lista_campos = [
        Frame_Atributo(janela_pessoa, "Primeiro Nome:",      pessoa.primeiro_nome),
        Frame_Atributo(janela_pessoa, "Apelido:",            pessoa.apelido),
        Frame_Atributo(janela_pessoa, "Data Nascimento:",    pessoa.data_nascimento),
        Frame_Atributo(janela_pessoa, "Morada:",             pessoa.morada),
        Frame_Atributo(janela_pessoa, "Altura:",             pessoa.altura) 
    ]

    """
    primeiro_nome = tk.Label(janela_pessoa, text = f"Primeiro Nome: {pessoa.primeiro_nome}")
    apelido = tk.Label(janela_pessoa,text = f"Apelido: {pessoa.apelido}")
    data_nascimento = tk.Label(janela_pessoa,text = f"Data Nascimento: {pessoa.data_nascimento}")
    morada = tk.Label(janela_pessoa,text = f"Morada: {pessoa.morada}")
    altura = tk.Label(janela_pessoa,text = f"Altura: {pessoa.altura}")
    """


    for campo in lista_campos:
        campo.pack()                        #Sem a função pack antes, aqui teria que fazer campo.frame.pack() 

    
    def toggle_edit():
        
        for campo in lista_campos:
            campo.toggle()                  #Toggle funciona de forma individual para cada frame

        if button["text"] == "Edit":
            button.config(text="Update")
            json_button.pack_forget()
        
        else:
            button.config(text="Edit")
            json_button.pack()

            try:
                pessoa.primeiro_nome = lista_campos[0].get_valor()
                pessoa.apelido = lista_campos[1].get_valor()

                try:
                    
                    data_str = lista_campos[2].get_valor()
                    pessoa.data_nascimento = datetime.strptime(data_str, "%Y-%m-%d").date()
                
                except Exception as erro_date:
                    messagebox.showerror("Error_date", f"Falha na data:\n{erro_date}")
                        
                    
                pessoa.morada = lista_campos[3].get_valor()
                pessoa.altura = lista_campos[4].get_valor()

            except Exception as erro:
                
                messagebox.showerror("Error", f"Falha na validação:\n {erro}")
                #Acabar a validação


    def to_json():

        with open("pessoa.json", "w") as f:
                json.dump(pessoa.to_dict(), f, indent=4, ensure_ascci=False)




    button = tk.Button(text="Edit", command=toggle_edit)
    button.pack()

    json_button = tk.Button(text="Save to .json File", command=to_json)
    json_button.pack()



    janela_pessoa.mainloop()






if __name__ == "__main__":

    pessoa_1 = Pessoa("Mozart","Amadeus",datetime(1756,1,27).date(),"Hagenauer Haus", 1.6)

    mostrar_pessoa(pessoa_1)