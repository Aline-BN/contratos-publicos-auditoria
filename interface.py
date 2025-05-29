import tkinter as tk
from tkinter import messagebox
import db
import ocorrencias
import interface_fiscais

def iniciar_interface():
    root = tk.Tk()
    root.title("Sistema de Contratos")
    root.geometry("1000x600")

    frame_campos = tk.Frame(root)
    frame_campos.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

    frame_botoes = tk.Frame(root)
    frame_botoes.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    campos = [
        ("Número do Contrato:", "entry_numero"),
        ("Empresa:", "entry_empresa"),
        ("Objeto:", "entry_objeto"),
        ("Valor:", "entry_valor"),
        ("Início (AAAA-MM-DD):", "entry_inicio"),
        ("Fim (AAAA-MM-DD):", "entry_fim"),
        ("Status:", "entry_status"),
        ("ID do Fiscal Responsável:", "entry_fiscal_id"),
        ("ID do Contrato para Excluir ou Editar:", "entry_id")
    ]
    entradas = {}

    for i, (label, var) in enumerate(campos):
        tk.Label(frame_campos, text=label).grid(row=i, column=0, sticky="w", pady=2)
        entradas[var] = tk.Entry(frame_campos, width=50)
        entradas[var].grid(row=i, column=1, pady=2)

    tk.Label(frame_campos, text="Lista de Contratos:").grid(row=len(campos), column=0, columnspan=2, pady=(10, 0), sticky="w")
    scrollbar = tk.Scrollbar(frame_campos)
    scrollbar.grid(row=len(campos)+1, column=2, sticky='ns')

    listbox = tk.Listbox(frame_campos, width=80, height=10, yscrollcommand=scrollbar.set)
    listbox.grid(row=len(campos)+1, column=0, columnspan=2, pady=5)
    scrollbar.config(command=listbox.yview)

    def inserir():
        try:
            numero = entradas["entry_numero"].get()
            empresa = entradas["entry_empresa"].get()
            objeto = entradas["entry_objeto"].get()
            valor = float(entradas["entry_valor"].get())
            inicio = entradas["entry_inicio"].get()
            fim = entradas["entry_fim"].get()
            status = entradas["entry_status"].get()
            fiscal_id = int(entradas["entry_fiscal_id"].get())

            if not all([numero, empresa, objeto, inicio, fim, status]):
                raise ValueError("Preencha todos os campos.")

            db.inserir_contrato(numero, empresa, objeto, valor, inicio, fim, status, fiscal_id)
            messagebox.showinfo("Sucesso", "Contrato inserido com sucesso!")
            listar()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar():
        listbox.delete(0, tk.END)
        contratos = db.listar_contratos()
        for c in contratos:
            fiscal = c[9] if c[9] else "Sem Fiscal"
            listbox.insert(tk.END, f"ID: {c[0]} | Nº: {c[1]} | Empresa: {c[2]} | Valor: R$ {c[4]:.2f} | Fiscal: {fiscal}")

    def excluir():
        try:
            id_contrato = int(entradas["entry_id"].get())
            linhas = db.excluir_contrato(id_contrato)
            if linhas == 0:
                messagebox.showinfo("Info", "Nenhum contrato encontrado.")
            else:
                messagebox.showinfo("Sucesso", "Contrato excluído.")
            listar()
        except ValueError:
            messagebox.showwarning("Atenção", "Informe um ID válido.")

    def editar():
        try:
            id_contrato = int(entradas["entry_id"].get())
            empresa = entradas["entry_empresa"].get()
            objeto = entradas["entry_objeto"].get()
            valor = float(entradas["entry_valor"].get())
            inicio = entradas["entry_inicio"].get()
            fim = entradas["entry_fim"].get()
            status = entradas["entry_status"].get()
            fiscal_id = int(entradas["entry_fiscal_id"].get())

            db.editar_contrato(id_contrato, empresa, objeto, valor, inicio, fim, status, fiscal_id)
            messagebox.showinfo("Sucesso", "Contrato editado com sucesso!")
            listar()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_botoes, text="Inserir Contrato", command=inserir, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Listar Contratos", command=listar, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Excluir Contrato", command=excluir, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Editar Contrato", command=editar, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Ocorrências", command=ocorrencias.janela_ocorrencias, width=20).pack(pady=5)
    tk.Button(frame_botoes, text="Fiscais", command=interface_fiscais.janela_fiscais, width=20).pack(pady=5)

    listar()
    root.mainloop()
