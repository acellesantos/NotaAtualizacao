# 🚀 Trello to Release Notes: Automação de Fluxo de Dados

Este projeto foi desenvolvido para resolver um problema real: o tempo gasto manualmente para compilar atualizações de software. Utilizei **Python** para criar um pipeline que extrai dados da **API do Trello**, organiza-os em **Excel** e os transforma em uma **interface HTML** pronta para o usuário final.

> **Impacto:** Redução de tarefas manuais e garantia de que nenhuma atualização seja publicada sem o protocolo correto ou imagem de evidência.

---

## 🛠️ Tecnologias e Conceitos Aplicados
Como desenvolvedora júnior, foquei em aplicar conceitos essenciais de engenharia de software neste projeto:

* **Consumo de APIs REST:** Uso da biblioteca `requests` para GET de dados, lidando com autenticação via Token/Key.
* **Manipulação de Dados:** Uso de `Pandas` para estruturação de dados e `Openpyxl` para formatação de planilhas.
* **Lógica de Automação:** Script orquestrador que conecta diferentes módulos do sistema.
* **Gestão de Variáveis de Ambiente:** Uso de `.env` para proteção de dados sensíveis (Segurança).
* **Frontend Dinâmico:** Geração de HTML via código, aplicando CSS inline para garantir a formatação no destino final.

## 📁 Estrutura do Repositório
O projeto é modularizado para facilitar a manutenção:
- `relatorio.py`: Módulo de extração (Trello -> DataFrame -> Excel).
- `nota.py`: Módulo de transformação (Excel -> HTML).
- `roda_tudo.py`: Script principal que executa o fluxo completo.

## ⚙️ Como rodar o projeto
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure suas chaves do Trello no arquivo `.env` (veja `.env.example`).
3. Execute o comando: `python roda_tudo.py`

## 💡 Aprendizados
Durante o desenvolvimento, superei desafios como:
- **Tratamento de exceções:** Garantir que o código não pare caso um card esteja sem solicitante ou sem imagem.
- **Tratamento de Strings:** Formatação de textos vindos da descrição do Trello para ficarem legíveis no HTML.
- **Experiência do Usuário (UX):** Criação de uma barra de progresso (`tqdm`) para dar feedback visual durante a extração dos dados.

---
**Desenvolvido por Marcelle Santos**
