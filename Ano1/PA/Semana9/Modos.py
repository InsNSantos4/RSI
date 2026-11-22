#from date import date
from date import date
from ex1 import Pessoa
import tkinter as tk
import json

class LabelEntry(tk.Frame):
    def __init__(self, parent, title, text, tipo="str"):
        super().__init__(parent)

        self.textvar = tk.StringVar()
        self.textvar.set(text)

        self.tipo = tipo              # tipo de validação: str, int, float, date
        self.valor_original = text    # usado para restaurar se inválido

        self.edit = False   # Modo Não-Edição

        self.lable_title = tk.Label(self, text=title)
        self.lable_text = tk.Label(self, text=text)
        self.entry= tk.Entry(self, textvariable=self.textvar)

        self.lable_title.pack(side=tk.LEFT) #Alinhado à esquerda do anterior (parent)
        self.lable_text.pack(side=tk.LEFT) #Alinhado à esquerda do anterior (entry)

    def entra_modo_edicao(self):
        if self.edit:
            return
        self.edit = True # Modo Edição

        self.lable_text.pack_forget()
        self.entry.pack(side=tk.LEFT)

    # criar outra função dentro da classe ->  sair_modo_edicao(self) :
    def sair_modo_edicao(self):
        if not self.edit:
            return
        self.edit = False

        #Atualiza o texto do label com o que está no Entry
        self.lable_text.config(text=self.textvar.get())

        novo_valor = self.textvar.get().strip()

        # -----------------------------
        # VALIDAÇÃO AUTOMÁTICA
        # -----------------------------
        if self.tipo == "int":
            try:
                v = int(novo_valor)
                if v < 1900 or v > date.now().year:
                    raise ValueError("Ano fora do intervalo válido.")
            except Exception:
                tk.messagebox.showerror("Erro", f"Valor inválido para ano: {novo_valor}")
                self.textvar.set(str(self.valor_original))
                novo_valor = self.valor_original

        elif self.tipo == "float":
            try:
                v = float(novo_valor)
                if v < 0.5 or v > 2.5:
                    raise ValueError("Altura fora do intervalo humano.")
            except Exception:
                tk.messagebox.showerror("Erro", f"Altura inválida: {novo_valor}")
                self.textvar.set(str(self.valor_original))
                novo_valor = self.valor_original

        elif self.tipo == "date":
            try:
                date.strptime(novo_valor, "%Y-%m-%d")
            except Exception:
                tk.messagebox.showerror("Erro", f"Data inválida (use YYYY-MM-DD): {novo_valor}")
                self.textvar.set(str(self.valor_original))
                novo_valor = self.valor_original

        elif self.tipo == "str":
            if novo_valor == "":
                tk.messagebox.showerror("Erro", "O campo não pode estar vazio.")
                self.textvar.set(str(self.valor_original))
                novo_valor = self.valor_original

        # Atualizar label e valor original
        self.valor_original = novo_valor
        self.label_text.config(text=str(novo_valor))

        # Trocar Entry → Label
        self.entry.pack_forget()        # faz o unpack da Entry
        self.lable_text.pack(side=tk.LEFT)  # faz o pack do texto da entry para uma label, ao trocar de modo



def show_person(person : Pessoa):
    mostra_pessoa = tk.Tk()     # cria objeto do tipo Janela gráfica
    mostra_pessoa.geometry("350x200")
    mostra_pessoa.title("Pessoa")
    

    # Para aparecer Pop-up:
    #tk.messagebox.showinfo("Pessoa:", person) 

    # widgets criados:
    first_name = LabelEntry(mostra_pessoa, "Primeiro Nome:", person.first_name, tipo="str")
    last_name = LabelEntry(mostra_pessoa, "Último Nome:", person.last_name, tipo="str")
    birthday = LabelEntry(mostra_pessoa, "Data de Nascimento:", person.birthdate, tipo="date")
    address = LabelEntry(mostra_pessoa, "Morada:", person.address, tipo="str")
    height = LabelEntry(mostra_pessoa, "Altura:", person.height, tipo="float")


    # entrar em modo Edição:
    def editar():
        first_name.entra_modo_edicao()
        last_name.entra_modo_edicao()
        birthday.entra_modo_edicao()
        address.entra_modo_edicao()
        height.entra_modo_edicao()

    # criar função visualizar() para entrar no modo de Visualização:
    def visualizar():
        first_name.sair_modo_edicao()
        last_name.sair_modo_edicao()
        birthday.sair_modo_edicao()
        address.sair_modo_edicao()
        height.sair_modo_edicao()


    # ---------------------------------------------------------
    # Função GUARDAR (Exercício 4)
    # ---------------------------------------------------------
    def guardar():
        # Primeiro sair do modo edição para validar tudo
        visualizar()

        # Recolher valores já validados
        dados = {
            "primeiro_nome": first_name.valor_original,
            "ultimo_nome": last_name.valor_original,
            "data_nascimento": birthday.valor_original,
            "morada": address.valor_original,
            "altura": height.valor_original
        }

        # Validar campos obrigatórios
        erros = []
        if dados["primeiro_nome"] == "":
            erros.append("Primeiro nome é obrigatório.")
        if dados["ultimo_nome"] == "":
            erros.append("Último nome é obrigatório.")
        if dados["morada"] == "":
            erros.append("Morada é obrigatória.")

        if erros:
            tk.messagebox.showerror("Erros", "\n".join(erros))
            return

        # Atualizar objeto Pessoa
        person.first_name = dados["primeiro_nome"]
        person.last_name = dados["ultimo_nome"]
        person.address = dados["morada"]
        person.height = float(dados["altura"])

        # Converter data
        try:
            person.birthdate = date.fromisoformat(str(dados["data_nascimento"]))
        except:
            pass  # já foi validado antes

        # Guardar em JSON
        with open("pessoa.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        tk.messagebox.showinfo("Sucesso", "Dados guardados em pessoa.json")    


    # Criar botão:
    b_edit = tk.Button(mostra_pessoa, text="Edit", command=editar)

    # Outro botão (para retomar ao modo de Visualização):
    b_visualize = tk.Button(mostra_pessoa, text="Visualizar", command=visualizar)

    tk.Button(mostra_pessoa, text="Guardar", command=guardar).pack(pady=5)


    b_edit.pack()                    # o pack renderiza por ordem
    b_visualize.pack()

    
    first_name.pack()
    last_name.pack()
    birthday.pack()
    address.pack()
    height.pack()

    mostra_pessoa.mainloop()    # ciclo infinito da janela (programa, depois de executado, só acaba quando eu clicar na cruz para fechar)


#código de teste do Modos.py:
if __name__ == "__main__":
    
    pessoa_1 = Pessoa("Rui", "Oliveira", date(2000, 5, 17), "Rua 25 abril", 1.90)
    show_person(pessoa_1)