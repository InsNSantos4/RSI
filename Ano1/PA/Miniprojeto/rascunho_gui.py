import tkinter as tk
from tkinter import ttk, messagebox
import json

# ── Dados mock ────────────────────────────────────────────────────────────────
hosts = [
    {"nome": "Server-01", "ip": "192.168.1.10", "permission": "admin"},
    {"nome": "PC-02",     "ip": "192.168.1.11", "permission": "user"},
    {"nome": "NAS-03",    "ip": "192.168.1.20", "permission": "user"},
]
admins = [
    {"nome": "Alice", "email": "alice@local", "smtp": "smtp.local", "permission": "admin"},
    {"nome": "Bob",   "email": "bob@local",   "smtp": "smtp.local", "permission": "admin"},
]


# ── Janela principal ──────────────────────────────────────────────────────────
main_window = tk.Tk()
main_window.title("Network Manager")
root.geometry("700x450")


# ── Funções de refresh ────────────────────────────────────────────────────────
def refresh():
    """Atualiza a Treeview com os hosts actuais."""
    for row in tree.get_children():
        tree.delete(row)
    for h in hosts:
        tree.insert("", "end", values=(h["nome"], h["ip"], h["permission"]))


def pesquisar():
    q = entry_pesquisa.get().strip().lower()
    for row in tree.get_children():
        tree.delete(row)
    for h in hosts:
        if q in h["nome"].lower() or q in h["ip"]:
            tree.insert("", "end", values=(h["nome"], h["ip"], h["permission"]))


def testar():
    q = entry_pesquisa.get().strip()
    encontrado = next((h for h in hosts if h["ip"] == q or h["nome"] == q), None)
    if encontrado:
        messagebox.showinfo("Testar", f"Host encontrado:\n{encontrado}")
    else:
        messagebox.showwarning("Testar", f"'{q}' não encontrado.")


def exportar():
    with open("network_export.json", "w", encoding="utf-8") as f:
        json.dump({"hosts": hosts, "admins": admins}, f, indent=2, ensure_ascii=False)
    messagebox.showinfo("Exportar", "Guardado em network_export.json")


# ── Sub-janela genérica ───────────────────────────────────────────────────────
def abrir_formulario(titulo, campos, ao_confirmar):
    """
    Cria uma janela com um formulário genérico.
    campos: lista de strings com os nomes dos campos
    ao_confirmar: função que recebe dict {campo: valor}
    """
    win = tk.Toplevel(root)
    win.title(titulo)
    win.resizable(False, False)

    entries = {}
    for i, campo in enumerate(campos):
        tk.Label(win, text=campo).grid(row=i, column=0, sticky="w", padx=12, pady=4)
        e = tk.Entry(win, width=24)
        e.grid(row=i, column=1, padx=12, pady=4)
        entries[campo] = e

    def confirmar():
        dados = {campo: e.get().strip() for campo, e in entries.items()}
        ao_confirmar(dados, win)

    tk.Button(win, text="Confirmar", command=confirmar)\
        .grid(row=len(campos), column=0, columnspan=2, pady=10)


# ── Lógica de cada acção ──────────────────────────────────────────────────────
def adicionar_host():
    def ao_confirmar(dados, win):
        if not dados["Nome"] or not dados["IP"]:
            messagebox.showerror("Erro", "Nome e IP são obrigatórios.", parent=win)
            return
        hosts.append({"nome": dados["Nome"], "ip": dados["IP"], "permission": dados["Permission"]})
        refresh()
        win.destroy()

    abrir_formulario("Adicionar Host", ["Nome", "IP", "Permission"], ao_confirmar)


def adicionar_admin():
    def ao_confirmar(dados, win):
        if not dados["Nome"]:
            messagebox.showerror("Erro", "Nome é obrigatório.", parent=win)
            return
        admins.append({"nome": dados["Nome"], "email": dados["Email"],
                       "smtp": dados["SMTP-server"], "permission": dados["Permission"]})
        refresh()
        win.destroy()

    abrir_formulario("Adicionar Admin", ["Nome", "Email", "SMTP-server", "Permission"], ao_confirmar)


def remover_host():
    def ao_confirmar(dados, win):
        h = next((h for h in hosts if h["nome"] == dados["Nome"]), None)
        if h:
            hosts.remove(h)
            refresh()
            win.destroy()
        else:
            messagebox.showerror("Erro", f"Host '{dados['Nome']}' não encontrado.", parent=win)

    abrir_formulario("Remover Host", ["Nome"], ao_confirmar)


def remover_admin():
    def ao_confirmar(dados, win):
        a = next((a for a in admins if a["nome"] == dados["Nome"]), None)
        if a:
            admins.remove(a)
            refresh()
            win.destroy()
        else:
            messagebox.showerror("Erro", f"Admin '{dados['Nome']}' não encontrado.", parent=win)

    abrir_formulario("Remover Admin", ["Nome"], ao_confirmar)


# ── Layout ────────────────────────────────────────────────────────────────────

# Barra de pesquisa
frame_top = tk.Frame(root)
frame_top.pack(fill="x", padx=10, pady=8)

tk.Label(frame_top, text="Pesquisa:").pack(side="left")
entry_pesquisa = tk.Entry(frame_top, width=30)
entry_pesquisa.pack(side="left", padx=4)
tk.Button(frame_top, text="Ok",     command=pesquisar).pack(side="left", padx=2)
tk.Button(frame_top, text="Testar", command=testar).pack(side="left", padx=2)

# Lista de Hosts (Treeview)
frame_mid = tk.Frame(root)
frame_mid.pack(fill="both", expand=True, padx=10)

tk.Label(frame_mid, text="Lista de Hosts", anchor="w").pack(fill="x")

cols = ("Nome", "IP", "Permissão")
tree = ttk.Treeview(frame_mid, columns=cols, show="headings", height=12)
for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=180)
tree.pack(fill="both", expand=True)

# Botões de acção
frame_bot = tk.Frame(root)
frame_bot.pack(fill="x", padx=10, pady=8)

tk.Button(frame_bot, text="Exportar",        command=exportar).pack(side="left", padx=4)
tk.Button(frame_bot, text="+ Adicionar Host",  command=adicionar_host).pack(side="left", padx=4)
tk.Button(frame_bot, text="+ Adicionar Admin", command=adicionar_admin).pack(side="left", padx=4)
tk.Button(frame_bot, text="- Remover Admin",   command=remover_admin).pack(side="left", padx=4)
tk.Button(frame_bot, text="- Remover Host",    command=remover_host).pack(side="left", padx=4)

# ── Arranque ──────────────────────────────────────────────────────────────────
refresh()
root.mainloop()