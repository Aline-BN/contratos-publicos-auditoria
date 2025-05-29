Sistema de Controle de Contratos Públicos

Aplicação desktop desenvolvida em Python com interface gráfica Tkinter e banco de dados SQLite. O sistema permite o gerenciamento de contratos administrativos, registro de ocorrências e controle dos fiscais responsáveis.

Descrição

Este sistema foi criado com o objetivo de facilitar a fiscalização e organização de contratos no setor público. O usuário pode cadastrar contratos com informações detalhadas, relacionar ocorrências a esses contratos e associar fiscais responsáveis, utilizando um banco de dados relacional com integridade garantida por chaves estrangeiras.

Funcionalidades

Módulo de Contratos
- Cadastro de contratos com número, empresa, objeto, valor, datas de vigência, status e fiscal responsável.
- Listagem dos contratos cadastrados com visualização simplificada.
- Edição de contratos por ID.
- Exclusão de contratos por ID.

Módulo de Ocorrências
- Cadastro de ocorrências vinculadas a contratos.
- Registro de tipo, data e descrição da ocorrência.
- Listagem e exclusão de ocorrências associadas.

Módulo de Fiscais
- Cadastro de fiscais com nome e matrícula.
- Listagem de fiscais cadastrados.
- Exclusão de fiscais por ID.

Banco de Dados

O banco de dados é criado automaticamente ao executar o sistema pela primeira vez.

Tecnologias Utilizadas

- Python 3
- Tkinter (GUI)
- SQLite3 (banco de dados)

Estrutura dos Arquivos

sistema-contratos/
│
├── db.py                  - Funções e estrutura do banco de dados
├── interface.py           - Tela principal para contratos
├── ocorrencias.py         - Interface de registro e visualização de ocorrências
├── interface_fiscais.py   - Interface de cadastro e controle de fiscais
├── main.py                - Arquivo principal de execução
└── README.txt             - Instruções e informações do projeto

Como Executar

1. Instale o Python 3, se ainda não estiver instalado.
2. Baixe ou clone este repositório.
3. Execute o arquivo principal no terminal:

   python main.py


Autoria

Desenvolvido por Aline Nascimento
Estudante de Ciência da Computação - CEUB | Servidora Pública
Contato: aline.b.nascimento@sempreceub.com
