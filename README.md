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


