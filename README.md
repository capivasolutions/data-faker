![Cover (1)](https://github.com/capivasolutions/data-faker/assets/31314944/c22bf113-a75a-470f-8792-90c803a9666d)

# 🧞‍♂️ Data Faker

Aplicação responsável por criar transações fakes a partir do Dataset original `creditcard.csv` e enviar ao back-end para processamento.

O dataset é carregado em memória, é realizado o oversample da classe fraudulenta com o SMOTE e são enviadas ao back-end em um intervalo pré definido.

## Requisitos

- [Python3](https://www.python.org/downloads/)
- Pip3
- [Python Virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

## Como executar

```bash
# Será necessário acessar fazer o download do dataset em https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
# Baixe o .zip, faça a extração do arquivo creditcard.csv e coloque-o em data/creditcard.csv

# Crie um arquivo .env na raiz do repositório e altere as variáveis (se necessário)
cp .env.example .env

# (Opcional) Crie um ambiente virtual com virtualenv
python3 -m venv venv
source venv/bin/activate

# Instale as dependências necessárias
pip3 install -r requirements.txt

# Execute o data-faker em ambiente de desenvolvimento
python3 src/main.py
```
