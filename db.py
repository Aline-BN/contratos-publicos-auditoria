import sqlite3

conexao = sqlite3.connect("contratos.db")
cursor = conexao.cursor()

# Criação das tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS fiscais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS contratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL,
    empresa TEXT NOT NULL,
    objeto TEXT NOT NULL,
    valor REAL NOT NULL,
    inicio TEXT NOT NULL,
    fim TEXT NOT NULL,
    status TEXT NOT NULL,
    fiscal_id INTEGER,
    FOREIGN KEY (fiscal_id) REFERENCES fiscais(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ocorrencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contrato_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (contrato_id) REFERENCES contratos(id)
)
""")

conexao.commit()

# Funções CRUD
def inserir_fiscal(nome, matricula):
    cursor.execute("INSERT INTO fiscais (nome, matricula) VALUES (?, ?)", (nome, matricula))
    conexao.commit()

def listar_fiscais():
    cursor.execute("SELECT * FROM fiscais")
    return cursor.fetchall()

def excluir_fiscal(id_fiscal):
    cursor.execute("DELETE FROM fiscais WHERE id = ?", (id_fiscal,))
    conexao.commit()
    return cursor.rowcount

def inserir_contrato(numero, empresa, objeto, valor, inicio, fim, status, fiscal_id):
    cursor.execute("""
        INSERT INTO contratos (numero, empresa, objeto, valor, inicio, fim, status, fiscal_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (numero, empresa, objeto, valor, inicio, fim, status, fiscal_id))
    conexao.commit()

def listar_contratos():
    cursor.execute("""
        SELECT contratos.id, contratos.numero, contratos.empresa,
               contratos.objeto, contratos.valor, contratos.inicio,
               contratos.fim, contratos.status, contratos.fiscal_id,
               fiscais.nome
        FROM contratos
        LEFT JOIN fiscais ON contratos.fiscal_id = fiscais.id
    """)
    return cursor.fetchall()

def excluir_contrato(id_contrato):
    cursor.execute("DELETE FROM contratos WHERE id = ?", (id_contrato,))
    conexao.commit()
    return cursor.rowcount

def editar_contrato(id_contrato, empresa, objeto, valor, inicio, fim, status, fiscal_id):
    cursor.execute("""
        UPDATE contratos
        SET empresa = ?, objeto = ?, valor = ?, inicio = ?, fim = ?, status = ?, fiscal_id = ?
        WHERE id = ?
    """, (empresa, objeto, valor, inicio, fim, status, fiscal_id, id_contrato))
    conexao.commit()

def inserir_ocorrencia(contrato_id, data, tipo, descricao):
    cursor.execute("""
        INSERT INTO ocorrencias (contrato_id, data, tipo, descricao)
        VALUES (?, ?, ?, ?)
    """, (contrato_id, data, tipo, descricao))
    conexao.commit()

def listar_ocorrencias(contrato_id):
    cursor.execute("SELECT * FROM ocorrencias WHERE contrato_id = ?", (contrato_id,))
    return cursor.fetchall()

def excluir_ocorrencia(id_ocorrencia):
    cursor.execute("DELETE FROM ocorrencias WHERE id = ?", (id_ocorrencia,))
    conexao.commit()
    return cursor.rowcount

def fechar_conexao():
    conexao.close()

