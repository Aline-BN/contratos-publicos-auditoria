
import sqlite3

# Conexão global
conexao = sqlite3.connect("contratos.db")
cursor = conexao.cursor()

# Criação das tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS contratos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL UNIQUE,
    empresa TEXT NOT NULL,
    objeto TEXT NOT NULL,
    valor REAL NOT NULL,
    inicio TEXT NOT NULL,
    fim TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ocorrencias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contrato_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (contrato_id) REFERENCES contratos(id)
)
""")

conexao.commit()

# Inserir contrato
def inserir_contrato(numero, empresa, objeto, valor, inicio, fim, status):
    cursor.execute("""
    INSERT INTO contratos (numero, empresa, objeto, valor, inicio, fim, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (numero, empresa, objeto, valor, inicio, fim, status))
    conexao.commit()

# Listar contratos
def listar_contratos():
    cursor.execute("SELECT * FROM contratos")
    return cursor.fetchall()

# Excluir contrato
def excluir_contrato(id_contrato):
    cursor.execute("DELETE FROM contratos WHERE id = ?", (id_contrato,))
    conexao.commit()
    return cursor.rowcount

# Fechar conexão
def fechar_conexao():
    conexao.close()
    
# Inserir ocorrência
def inserir_ocorrencia(contrato_id, data, tipo, descricao):
    cursor.execute("""
        INSERT INTO ocorrencias (contrato_id, data, tipo, descricao)
        VALUES (?, ?, ?, ?)
    """, (contrato_id, data, tipo, descricao))
    conexao.commit()

# Listar ocorrências de um contrato
def listar_ocorrencias_por_contrato(contrato_id):
    cursor.execute("""
        SELECT id, data, tipo, descricao
        FROM ocorrencias
        WHERE contrato_id = ?
    """, (contrato_id,))
    return cursor.fetchall()

# Excluir ocorrência
def excluir_ocorrencia(id_ocorrencia):
    cursor.execute("DELETE FROM ocorrencias WHERE id = ?", (id_ocorrencia,))
    conexao.commit()
    return cursor.rowcount
