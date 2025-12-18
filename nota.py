import os
import pandas as pd
from datetime import datetime

# ===== CONFIGURAÇÕES =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_PLANILHAS = os.path.join(BASE_DIR, "Planilhas")
PASTA_NOTAS = os.path.join(BASE_DIR, "Notas")

# ===== LOCALIZA PLANILHA MAIS RECENTE =====
def obter_planilha_recente(pasta):
    arquivos = [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.endswith(".xlsx")
    ]
    if not arquivos:
        raise FileNotFoundError("Nenhuma planilha .xlsx encontrada na pasta.")
    return max(arquivos, key=os.path.getmtime)

# ===== LÊ PLANILHA =====
arquivo_planilha = obter_planilha_recente(PASTA_PLANILHAS)

df = pd.read_excel(arquivo_planilha, keep_default_na=False).fillna("")

# ===== DIAGNÓSTICO E FILTRAGEM (MANTENDO AS MELHORIAS DE ROBUSTEZ) =====

# Adiciona .astype(str) novamente por segurança, mas o filtro permanece.
df_tipo_upper = df["Tipo"].astype(str).str.strip().str.upper()

# 🛑 NOVO DIAGNÓSTICO COMPLETO 🛑
print("--- DIAGNÓSTICO DO DATAFRAME ---")
print("1. Colunas Encontradas: OK")
print("\n2. Valores Únicos (e suas contagens) na coluna 'Tipo':")
valores_tipo = df_tipo_upper.value_counts()
if not valores_tipo.empty:
    for tipo, contagem in valores_tipo.items():
        print(f" - {tipo}: {contagem} itens")
    # Se há mais de 100 tipos únicos, imprima um aviso
    if len(valores_tipo) > 100:
        print("\nAtenção: Muitas variações na coluna 'Tipo'. Verifique a consistência dos dados.")
else:
    print("A coluna 'Tipo' está vazia ou não possui valores detectáveis.")
print("--------------------------------\n")


# ===== SEPARA POR TIPO (USANDO O FILTRO CORRIGIDO) =====
df_inov = df[df_tipo_upper.str.contains("INOVA", na=False)]
df_corr = df[df_tipo_upper.str.contains("CORRE", na=False)]

# ==== VERIFICAÇÃO DE DADOS (Resto do Script) =====
print(f"--- Verificação de Dados ---")
print(f"|   Inovações encontradas: {len(df_inov)} itens.")
print(f"|   Correções encontradas: {len(df_corr)} itens.")
print(f"----------------------------")

# ===== FUNÇÃO PARA GERAR LISTAS SIMPLES =====
def gerar_lista(df):
    lista = ""
    for _, row in df.iterrows():
        titulo = row["Título do card"]
        link_card = row["Link do card"]
        lista += f'<li><a href="{link_card}" target="_blank" rel="noreferrer noopener">{titulo}</a></li>\n'
    return lista

# ===== FUNÇÃO PARA GERAR TAG DE IMAGEM =====
def gerar_tag_imagem(url):
    if url and str(url).strip():
        return f'<p><img src="{url}" alt="Imagem do comentário" width="800" style="height:auto;" /></p>'
    return ""

# ===== BLOCO MODELO PARA INOVAÇÕES =====
bloco_inov = """
<p><span style="background-color: #adffc1;"><strong>-&gt;&nbsp;</strong><strong>{titulo}:</strong></span></p>
<p><em><strong>Solicitante:</strong>&nbsp;{solicitante} -&nbsp;<strong>Chamado:</strong>&nbsp;</em><em>{protocolo}</em></p>
<p><strong>Pedido:</strong>&nbsp;{pedido}</p>
<p><strong>Observação:</strong>&nbsp;{observacao}</p>
{imagem}
<p><strong>Data da conclusão:</strong><em>&nbsp;{data}.</em></p>
<p>&nbsp;</p>
"""

# ===== BLOCO MODELO PARA CORREÇÕES =====
bloco_corr = """
<p><span style="background-color: #adffc1;"><strong>-&gt;&nbsp;</strong><strong>{titulo}:</strong></span></p>
<p><em><strong>Solicitante:</strong>&nbsp;{solicitante} -&nbsp;<strong>Chamado:</strong>&nbsp;</em><em>{protocolo}</em></p>
<p><strong>Problema:</strong>&nbsp;{pedido}</p>
<p><strong>Observação:</strong>&nbsp;{observacao}</p>
{imagem}
<p><strong>Data da conclusão:</strong><em>&nbsp;{data}.</em></p>
<p>&nbsp;</p>
"""

# ===== BLOCO HTML PRINCIPAL =====
html = f"""<p><a href="https://servicedesk.clinicacamim.com.br/" target="_blank" rel="noreferrer noopener"><img src="" alt="" width="800" /></a></p>
<p style="padding-left: 40px; text-align: center;"><span style="text-decoration: underline;"><span style="color: #035d10;"><strong style="font-size: 18.6667px;">LISTA DE CARDS</strong></span></span></p>
<p style="text-align: left; padding-left: 40px;"><span style="color: #000000; background-color: #00ff2a;"><strong>INOVAÇÕES</strong></span></p>
<ol>
{gerar_lista(df_inov)}
</ol>
<p style="text-align: left; padding-left: 40px;"><span style="color: #000000; background-color: #00ff2a;"><strong><span style="text-decoration: underline;">CORREÇÕES</span></strong></span></p>
<ol>
{gerar_lista(df_corr)}
</ol>
<p style="text-align: center;"><span style="text-decoration: underline; color: #035d10;"><span style="font-size: 14pt;"><strong>NOTA DE ATUALIZAÇÃO</strong></span></span></p>
<p style="text-align: center;"><span style="background-color: #00ff2a;"><strong>INOVAÇÕES</strong></span></p>
"""

# ===== ADICIONA INOVAÇÕES =====
for _, row in df_inov.iterrows():
    solicitante = row.get("Solicitante", "").strip() or "Victoria Utrini"
    html += bloco_inov.format(
        titulo=row["Título do card"],
        solicitante=solicitante,
        protocolo=row.get("Protocolo", ""),
        pedido=row.get("Pedido", ""),
        observacao=row.get("Observação", ""),
        imagem=gerar_tag_imagem(row.get("Imagem Observação", "")),
        data=row.get("Data do DONE", "")
    )

# ===== ADICIONA CORREÇÕES =====
html += '<p style="text-align: center;"><span style="text-decoration: underline; background-color: #00ff2a;"><strong>CORREÇÕES</strong></span></p>\n'
for _, row in df_corr.iterrows():
    solicitante = row.get("Solicitante", "").strip() or "Victoria Utrini"
    html += bloco_corr.format(
        titulo=row["Título do card"],
        solicitante=solicitante,
        protocolo=row.get("Protocolo", ""),
        pedido=row.get("Pedido", ""),
        observacao=row.get("Observação", ""),
        imagem=gerar_tag_imagem(row.get("Imagem Observação", "")),
        data=row.get("Data do DONE", "")
    )

# ===== GERA NOME COM DATA =====
data_atual = datetime.now().strftime("%d%m%Y-%H%M")
NOME_SAIDA = os.path.join(PASTA_NOTAS, f"nota_atualizacao{data_atual}.html")

# ===== SALVA ARQUIVO =====
with open(NOME_SAIDA, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML gerado com sucesso: {NOME_SAIDA}")
print(f"📄 Planilha usada: {os.path.basename(arquivo_planilha)}")
print("Agora é só abrir o arquivo no navegador e copiar o código-fonte (Source Code) para o HESK.")
