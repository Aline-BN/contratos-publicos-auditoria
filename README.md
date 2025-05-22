## Sistema de Controle de Contratos Públicos com Registro de Ocorrências

Este projeto é uma aplicação desktop desenvolvida em Python, utilizando Tkinter para a interface gráfica e SQLite como banco de dados.  
Seu foco principal é facilitar o gerenciamento de contratos administrativos e o registro de ocorrências contratuais — como glosas, multas, advertências e atrasos — de forma simples, direta e organizada.

### Com ele, é possível:

- Cadastrar, visualizar e excluir contratos com facilidade;
- Registrar e acompanhar ocorrências associadas a cada contrato;
- Navegar por uma interface gráfica prática e funcional;
- Armazenar e relacionar dados com segurança, utilizando chave estrangeira.

---

## Tecnologias Utilizadas

- Python 3
- Tkinter (Interface Gráfica)
- SQLite3 (Banco de Dados)

---

## Funcionalidades

### Módulo de Contratos

- Cadastro de novos contratos (número, empresa, valor, vigência e status);
- Listagem de todos os contratos registrados;
- Exclusão de contratos por ID.

### Módulo de Ocorrências

- Janela dedicada para gerenciamento de ocorrências;
- Seleção de contrato por número ou nome da empresa;
- Registro detalhado de ocorrências (data, tipo e descrição);
- Visualização de todas as ocorrências relacionadas a um contrato;
- Exclusão de ocorrências por ID.

---

## Estrutura de Arquivos

sistema-contratos/
├── db.py # Funções e criação do banco SQLite
├── interface.py # Tela principal para contratos
├── ocorrencias.py # Janela de ocorrências vinculadas a contratos
├── main.py # Ponto de entrada do sistema
├── contratos.db # Banco de dados gerado automaticamente
└── README.md # Este arquivo

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone o repositório ou baixe os arquivos `.py`.
3. No terminal, execute:

python main.py

Autora
Desenvolvido por Aline Nascimento – Estudante de Ciência da Computação e Servidora Pública.


Contato
LinkedIn: www.linkedin.com/in/alinebornascimento

Email: aline.b.nascimento@sempreceub.com

