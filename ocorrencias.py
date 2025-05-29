import tkinter as tk
from tkinter import messagebox
import db

def janela_ocorrencias():
    janela = tk.Toplevel()
    janela.title("Gerenciar Ocorrências")
    janela.geometry("1000x500")

    frame_campos = tk.Frame(janela)
    frame_campos.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

    frame_botoes = tk.Frame(janela)
    frame_botoes.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    
    campos = [
        ("ID do Contrato:", "entry_id_contrato"),
        ("Data (AAAA-MM-DD):", "entry_data"),
        ("Tipo:", "entry_tipo"),
        ("Descrição:", "entry_descricao"),
        ("ID para excluir:", "entry_id_excluir")
    ]
    entradas = {}

    for i, (label, var) in enumerate(campos):
        tk.Label(frame_campos, text=label).grid(row=i, column=0, sticky="w", pady=2)
        if "descricao" in var:
            entradas[var] = tk.Text(frame_campos, height=4, width=50)
            entradas[var].grid(row=i, column=1, pady=2)
        else:
            entradas[var] = tk.Entry(frame_campos, width=50)
            entradas[var].grid(row=i, column=1, pady=2)

    # Listbox com scrollbar
    tk.Label(frame_campos, text="Lista de Ocorrências:").grid(row=len(campos), column=0, columnspan=2, pady=(10, 0), sticky="w")
    scrollbar = tk.Scrollbar(frame_campos)
    scrollbar.grid(row=len(campos)+1, column=2, sticky='ns')
    listbox = tk.Listbox(frame_campos, width=80, height=10, yscrollcommand=scrollbar.set)
    listbox.grid(row=len(campos)+1, column=0, columnspan=2, pady=5)
    scrollbar.config(command=listbox.yview)

    def inserir():
        try:
            contrato_id = int(entradas["entry_id_contrato"].get())
            data = entradas["entry_data"].get()
            tipo = entradas["entry_tipo"].get()
            descricao = entradas["entry_descricao"].get("1.0", tk.END).strip()

            db.inserir_ocorrencia(contrato_id, data, tipo, descricao)
            listar()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir():
        try:
            id_ocorrencia = int(entradas["entry_id_excluir"].get())
            linhas = db.excluir_ocorrencia(id_ocorrencia)
            if linhas == 0:
                messagebox.showinfo("Info", "Nenhuma ocorrência encontrada.")
            else:
                messagebox.showinfo("Sucesso", "Ocorrência excluída.")
            listar()
        except ValueError:
            messagebox.showwarning("Atenção", "Informe um ID válido.")

    def listar():
        try:
            contrato_id = int(entradas["entry_id_contrato"].get())
            ocorrencias = db.listar_ocorrencias(contrato_id)
            listbox.delete(0, tk.END)
            for o in ocorrencias:
                listbox.insert(tk.END, f"ID: {o[0]} | Data: {o[2]} | Tipo: {o[3]} | Desc: {o[4]}")
        except ValueError:
            listbox.delete(0, tk.END)

    # Botões
    tk.Button(frame_botoes, text="Inserir Ocorrência", command=inserir, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Excluir Ocorrência", command=excluir, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Listar Ocorrências", command=listar, width=20).pack(pady=5)

    listar()
