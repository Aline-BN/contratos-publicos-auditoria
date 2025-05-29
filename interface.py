import tkinter as tk
from tkinter import messagebox
import db

def janela_fiscais():
    janela = tk.Toplevel()
    janela.title("Gerenciar Fiscais")
    janela.geometry("700x400")

    frame_campos = tk.Frame(janela)
    frame_campos.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

    frame_botoes = tk.Frame(janela)
    frame_botoes.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    # Campos
    tk.Label(frame_campos, text="Nome do Fiscal:").grid(row=0, column=0, sticky="w", pady=2)
    entry_nome = tk.Entry(frame_campos, width=40)
    entry_nome.grid(row=0, column=1, pady=2)

    tk.Label(frame_campos, text="Matrícula:").grid(row=1, column=0, sticky="w", pady=2)
    entry_matricula = tk.Entry(frame_campos, width=40)
    entry_matricula.grid(row=1, column=1, pady=2)

    tk.Label(frame_campos, text="ID para excluir:").grid(row=2, column=0, sticky="w", pady=2)
    entry_id = tk.Entry(frame_campos, width=20)
    entry_id.grid(row=2, column=1, sticky="w", pady=2)

    # Listbox com rolagem
    tk.Label(frame_campos, text="Lista de Fiscais:").grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="w")
    scrollbar = tk.Scrollbar(frame_campos)
    scrollbar.grid(row=4, column=2, sticky='ns')
    listbox = tk.Listbox(frame_campos, width=60, height=10, yscrollcommand=scrollbar.set)
    listbox.grid(row=4, column=0, columnspan=2, pady=5)
    scrollbar.config(command=listbox.yview)

    def inserir():
        nome = entry_nome.get()
        matricula = entry_matricula.get()
        if nome == "" or matricula == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return
        db.inserir_fiscal(nome, matricula)
        listar()
        entry_nome.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)

    def excluir():
        try:
            id_fiscal = int(entry_id.get())
            linhas = db.excluir_fiscal(id_fiscal)
            if linhas == 0:
                messagebox.showinfo("Info", "Nenhum fiscal encontrado.")
            else:
                messagebox.showinfo("Sucesso", "Fiscal excluído.")
            listar()
        except ValueError:
            messagebox.showwarning("Atenção", "Informe um ID válido.")

    def listar():
        listbox.delete(0, tk.END)
        fiscais = db.listar_fiscais()
        for f in fiscais:
            listbox.insert(tk.END, f"ID: {f[0]} | Nome: {f[1]} | Matrícula: {f[2]}")

    # Botões
    tk.Button(frame_botoes, text="Inserir Fiscal", command=inserir, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Excluir Fiscal", command=excluir, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Listar Fiscais", command=listar, width=20).pack(pady=5)

    listar()
