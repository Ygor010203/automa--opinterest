"""
Converte o produtos.csv (usado pelo bot do Telegram) para o formato
EXATO que o importador em massa do Pinterest exige.

IMPORTANTE: antes de importar, crie o quadro (board) manualmente no
Pinterest com o nome exato usado em NOME_DO_QUADRO abaixo. O Pinterest
pode não criar o quadro sozinho a partir do CSV.

COMO USAR:
py gerar_feed_pinterest.py

Gera o arquivo "feed_pinterest.csv", pronto para subir em:
pinterest.com/pin-builder (ou na tela "Criar vários Pins")
"""

import csv

ARQUIVO_ENTRADA = "produtos.csv"
ARQUIVO_SAIDA = "feed_pinterest.csv"
NOME_DO_QUADRO = "Achadinhos Mercado Livre BH"  # ajuste para o nome exato do seu board

# Cabeçalho EXATO exigido pelo Pinterest (atenção ao espaço em "Media URL")
COLUNAS_PINTEREST = [
    "Title",
    "Media URL",
    "Pinterest board",
    "Description",
    "Link",
    "Publish date",
    "Keywords",
]

produtos_convertidos = []
titulos_ja_usados = set()  # evita o erro "Várias linhas com o mesmo título"

with open(ARQUIVO_ENTRADA, encoding="utf-8-sig", newline="") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        nome = linha.get("nome", "").strip()
        preco = linha.get("preco", "").strip()
        descricao = linha.get("descricao", "").strip()
        link = linha.get("link", "").strip()
        imagem = (linha.get("imagem") or linha.get("fotos") or "").strip()

        if not nome or not imagem or not link:
            continue  # pula produto incompleto, evita pin quebrado

        if nome in titulos_ja_usados:
            continue  # pula duplicata de título, o Pinterest rejeita isso
        titulos_ja_usados.add(nome)

        produtos_convertidos.append({
            "Title": nome[:100],  # Pinterest limita título a 100 caracteres
            "Media URL": imagem,
            "Pinterest board": NOME_DO_QUADRO,
            "Description": f"{descricao} - R$ {preco}"[:500],  # limite de 500 caracteres
            "Link": link,
            "Publish date": "",  # vazio = publica assim que for aprovado
            "Keywords": "",      # opcional, pode preencher depois
        })

with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=COLUNAS_PINTEREST)
    escritor.writeheader()
    for produto in produtos_convertidos:
        escritor.writerow(produto)

print(f"Sucesso! {len(produtos_convertidos)} produtos convertidos em {ARQUIVO_SAIDA}")
print(f"Lembre-se: crie o quadro '{NOME_DO_QUADRO}' manualmente no Pinterest antes de importar.")