# 🚀 Trello to HESK Automation: RPA de Release Notes

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)](https://trello.com/)

> **Status do Projeto:** Concluído ✅

Este projeto nasceu para resolver uma dor real no meu cotidiano profissional: o processo manual, lento e repetitivo de compilar atualizações de software. Utilizei **Python** para criar um pipeline automatizado que extrai dados da **API do Trello**, organiza-os via **Pandas** e os transforma em uma interface **HTML** pronta para publicação no sistema HESK.

**📈 Impacto:** Automação completa do fluxo quinzenal, garantindo padronização visual e 0% de erro humano na transferência de dados.

---

## 🛠️ Tecnologias e Conceitos Aplicados

Como desenvolvedora junior, foquei em aplicar conceitos sólidos de engenharia de software:

* **🌐 Consumo de APIs REST:** Uso da biblioteca `requests` para extração de dados, lidando com autenticação e endpoints dinâmicos.
* **📊 Manipulação de Dados:** Uso de `Pandas` para estruturação e `Openpyxl` para formatação avançada de planilhas.
* **🔒 Segurança:** Gestão de variáveis de ambiente com `.env` para proteção de Tokens e chaves de API.
* **🎨 Frontend Dinâmico:** Geração de estruturas HTML via código com CSS inline para compatibilidade total.

---

## 📁 Estrutura do Repositório

O projeto é modularizado para facilitar a manutenção e escalabilidade:

| Arquivo | Função |
| :--- | :--- |
| `relatorio.py` | Extração de dados (Trello ➡️ DataFrame ➡️ Excel). |
| `nota.py` | Transformação de dados (Excel ➡️ HTML). |
| `roda_tudo.py` | Script orquestrador (Execução do fluxo completo). |

---

## 💡 Aprendizados e Desafios

Durante o desenvolvimento, superei desafios técnicos que elevaram meu nível como programadora:
* **Tratamento de Exceções:** Implementação de verificações para garantir que o código não pare caso um card esteja incompleto ou sem imagem.
* **UX no Terminal:** Adição da biblioteca `tqdm` para exibir uma barra de progresso, oferecendo feedback visual durante a execução.
* **Sanitização de Strings:** Tratamento de caracteres especiais e formatação de textos vindos do Trello para exibição limpa no HTML.

---

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/acellesantos/trello-to-hesk-automation.git](https://github.com/acellesantos/trello-to-hesk-automation.git)
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Configure suas credenciais no arquivo `.env` (baseie-se no `.env.example`).
4. Execute o orquestrador:
   ```bash
   python roda_tudo.py

---

<p align="center">Desenvolvido com ☕ e 🐍 por <b>Marcelle Santos</b></p>
