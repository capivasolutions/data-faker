# 🃏 Data Faker

Aplicação responsável por gerar transações fakes a partir do Dataset original `creditcard.csv` e enviar ao back-end para processamento.

## Requisitos

- Python3
- Pip3
- Python Virtualenv

## Como executar

```bash
# Crie um arquivo .env na raiz do repositório e altere as variáveis (se necessário)
cp .env.example .env

# (Opcional) Crie um ambiente virtual com virtualenv
python -m venv venv
source venv/bin/Activate

# Instale as dependências necessárias
pip3 install -r requirements.txt

# Execute o data-faker em ambiente de desenvolvimento
python3 src/main.py
```
