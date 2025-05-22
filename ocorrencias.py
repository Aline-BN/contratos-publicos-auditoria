
import tkinter as tk
from tkinter import messagebox, ttk
import db

def janela_ocorrencias():
    janela = tk.Toplevel()
    janela.title("Gerenciar Ocorrências")
    janela.geometry("700x600")

    contratos = db.listar_contratos()
    contratos_dict = {f"{c[1]} - {c[2]}": c[0] for c in contratos}

    # Widgets para seleção do contrato
    tk.Label(janela, text="Selecione um Contrato:").pack(pady=5)
    contrato_var = tk.StringVar()
    contrato_menu = ttk.Combobox(janela, textvariable=contrato_var, values=list(contratos_dict.keys()), state='readonly', width=60)
    contrato_menu.pack(pady=5)

    # Campos de ocorrência
    tk.Label(janela, text="Data (YYYY-MM-DD):").pack()
    entry_data = tk.Entry(janela)
    entry_data.pack()

    tk.Label(janela, text="Tipo (glosa, multa, etc.):").pack()
    entry_tipo = tk.Entry(janela)
    entry_tipo.pack()

    tk.Label(janela, text="Descrição:").pack()
    entry_desc = tk.Entry(janela, width=60)
    entry_desc.pack()

    def inserir_ocorrencia():
        contrato_selecionado = contrato_var.get()
        if not contrato_selecionado:
            messagebox.showwarning("Atenção", "Selecione um contrato.")
            return

        contrato_id = contratos_dict[contrato_selecionado]
        data = entry_data.get()
        tipo = entry_tipo.get()
        descricao = entry_desc.get()

        if not all([data, tipo, descricao]):
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        db.inserir_ocorrencia(contrato_id, data, tipo, descricao)
        messagebox.showinfo("Sucesso", "Ocorrência registrada.")
        entry_data.delete(0, tk.END)
        entry_tipo.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
        listar_ocorrencias()

    tk.Button(janela, text="Registrar Ocorrência", command=inserir_ocorrencia).pack(pady=10)

    # Lista de ocorrências
    tk.Label(janela, text="Ocorrências registradas:").pack()
    listbox = tk.Listbox(janela, width=100)
    listbox.pack(pady=10)

    def listar_ocorrencias():
        listbox.delete(0, tk.END)
        contrato_selecionado = contrato_var.get()
        if contrato_selecionado:
            contrato_id = contratos_dict[contrato_selecionado]
            ocorrencias = db.listar_ocorrencias_por_contrato(contrato_id)
            for o in ocorrencias:
                listbox.insert(tk.END, f"ID: {o[0]} | {o[1]} | {o[2]} | {o[3]}")

    def excluir_ocorrencia():
        selecao = listbox.curselection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma ocorrência na lista.")
            return
        linha = listbox.get(selecao[0])
        id_ocorrencia = linha.split('|')[0].replace("ID:", "").strip()
        if db.excluir_ocorrencia(id_ocorrencia):
            messagebox.showinfo("Sucesso", f"Ocorrência {id_ocorrencia} excluída.")
        else:
            messagebox.showwarning("Erro", "Ocorrência não encontrada.")
        listar_ocorrencias()

    tk.Button(janela, text="Excluir Ocorrência Selecionada", command=excluir_ocorrencia).pack(pady=5)
    contrato_menu.bind("<<ComboboxSelected>>", lambda e: listar_ocorrencias())