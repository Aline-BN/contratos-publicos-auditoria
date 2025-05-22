import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

import sqlite3
import db  # nome do módulo do banco
import ocorrencias 

def iniciar_interface():
    root = tk.Tk()
    root.title("Sistema de Contratos")
    root.geometry("600x600")

    # Funções internas
    def inserir():
        numero = entry_numero.get()
        empresa = entry_empresa.get()
        objeto = entry_objeto.get()
        valor = entry_valor.get()
        inicio = entry_inicio.get()
        fim = entry_fim.get()
        status = entry_status.get()

        if not all([numero, empresa, objeto, valor, inicio, fim, status]):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            valor_float = float(valor)
            db.inserir_contrato(numero, empresa, objeto, valor_float, inicio, fim, status)
            messagebox.showinfo("Sucesso", f"Contrato {numero} inserido!")
            for entry in [entry_numero, entry_empresa, entry_objeto, entry_valor, entry_inicio, entry_fim, entry_status]:
                entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Valor deve ser um número válido")
        listar()

    def listar():
        listbox.delete(0, tk.END)
        contratos = db.listar_contratos()
        for c in contratos:
            listbox.insert(tk.END, f"ID: {c[0]} | Nº: {c[1]} | Empresa: {c[2]} | Valor: R$ {c[4]:.2f}")

    def excluir():
        id_contrato = entry_id.get()
        if id_contrato == "":
            messagebox.showwarning("Atenção", "Informe o ID para excluir!")
            return
        linhas_excluidas = db.excluir_contrato(id_contrato)
        if linhas_excluidas == 0:
            messagebox.showinfo("Info", "Nenhum contrato com esse ID.")
        else:
            messagebox.showinfo("Sucesso", f"Contrato com ID {id_contrato} excluído")
        entry_id.delete(0, tk.END)
        listar()

    # Widgets de entrada
    tk.Label(root, text="Número do Contrato:").pack()
    entry_numero = tk.Entry(root)
    entry_numero.pack()

    tk.Label(root, text="Empresa:").pack()
    entry_empresa = tk.Entry(root)
    entry_empresa.pack()

    tk.Label(root, text="Objeto:").pack()
    entry_objeto = tk.Entry(root)
    entry_objeto.pack()

    tk.Label(root, text="Valor (R$):").pack()
    entry_valor = tk.Entry(root)
    entry_valor.pack()

    tk.Label(root, text="Data Início (YYYY-MM-DD):").pack()
    entry_inicio = tk.Entry(root)
    entry_inicio.pack()

    tk.Label(root, text="Data Fim (YYYY-MM-DD):").pack()
    entry_fim = tk.Entry(root)
    entry_fim.pack()

    tk.Label(root, text="Status:").pack()
    entry_status = tk.Entry(root)
    entry_status.pack()

    tk.Button(root, text="Inserir Contrato", command=inserir).pack(pady=10)

    # Lista de contratos
    tk.Label(root, text="Contratos Cadastrados:").pack()
    listbox = tk.Listbox(root, width=80)
    listbox.pack(pady=5)

    # Exclusão
    tk.Label(root, text="ID do Contrato para excluir:").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()

    tk.Button(root, text="Excluir Contrato", command=excluir).pack(pady=10)

    tk.Button(root, text="Gerenciar Ocorrências", command=ocorrencias.janela_ocorrencias).pack(pady=10)

    listar()
    root.mainloop()