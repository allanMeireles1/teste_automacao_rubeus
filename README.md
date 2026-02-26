# Desafio Técnico - Analista de Qualidade Júnior | Rubeus

Este repositório contém a entrega do teste prático para o processo seletivo da **Rubeus**.
O projeto consiste na análise de qualidade, identificação de bugs e sugestões de melhoria em duas páginas de exemplo, além da automação dos fluxos principais utilizando **Python** e **Playwright**.

---

## 📋 Escopo do Teste

A análise foi realizada nas seguintes URLs:

1. **Certificação**
   https://qualidade.apprbs.com.br/certificacao

2. **Site Institucional**
   https://qualidade.apprbs.com.br/site

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework de Automação:** Playwright
* **Controle de Versão:** Git

---

## 📂 Estrutura do Projeto

```text
teste_automacao/
├── site_certificacao/
│   └── test_certificacao.py   # Scripts automatizados da página de certificação
├── site_institucional/
│   └── test_site.py           # Scripts automatizados do site principal
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação principal
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/allanMeireles1/NOME_DO_REPO.git
cd desafio-qa-rubeus
```

---

### 2. Criar ambiente virtual (Linux Mint)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
playwright install
```

---

### 4. Executar testes

```bash
pytest
```

---

## 👤 Candidato

**Nome:** Allan Meireles
**LinkedIn:** https://linkedin.com/in/allan-meireles-qa/

