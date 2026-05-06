# 💰 API de Controle Financeiro

Essa API foi desenvolvida com FastAPI e SQLAlchemy para gerenciamento de transações financeiras pessoais, com foco em organização de gastos, controle de receitas e análise de dados.

---

## 🚀 Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn

---

## 📌 Funcionalidades

### 🧾 CRUD de Transações
- Criar transação
- Listar transações
- Buscar transação por ID
- Atualizar transação
- Deletar transação

### 📊 Dashboard Financeiro
- Total de receitas (income)
- Total de despesas (expense)
- Saldo geral
- Gastos por categoria

---

## 🧠 Regras de negócio

- Toda transação deve ser classificada como:
  - `income` (entrada de dinheiro)
  - `expense` (saída de dinheiro)

- O saldo é calculado automaticamente:
  - `saldo = income - expense`

- O dashboard é baseado exclusivamente nas transações registradas no banco de dados

- Valores monetários são armazenados como `float`

---

## 📁 Estrutura do projeto

```bash
API-Gastos/
│
├── codigo/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   └── transaction.py
│   │
│   ├── routes/
│   │   └── transaction_routes.py
│   │
│   └── services/
│       └── transaction_service.py
│
├── .env
├── requirements.txt
├── README.md
```

---

## ⚙️ Como rodar o projeto

### Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- Python 3.10+
- MySQL instalado e rodando
- Git
- pip (já vem com Python)

### 1. Clonar o repositório

```bash
git clone https://github.com/moisesmaaia/API-de-gastos.git
cd API-de-Gastos
cd codigo
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r ..\requirements.txt
```

### 4. Configurar banco de dados

Crie um arquivo `.env` na raiz do projeto e adicione:

```bash
DATABASE_URL = "mysql+pymysql://root:sua_senha@localhost/nome_do_banco"
```

### 5. Rodar aplicação

```bash
uvicorn main:app --reload
```

### 6. Acessar documentação

``` bash
http://127.0.0.1:8000/docs
```

# 📊 Endpoints principais

### Transações
- `GET /transactions`
- `GET /transactions/{id}`
- `POST /transactions`
- `PUT /transactions/{id}`
- `DELETE /transactions/{id}`

### Dashboard
- `GET /dashboard`


