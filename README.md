# 📌 Pinterest CSV Feed Generator

Script em Python desenvolvido para converter o arquivo de produtos (`produtos.csv`) de um bot de ofertas do Telegram no formato **exato** exigido pelo importador em massa do Pinterest (`feed_pinterest.csv`).

## 🚀 O que ele faz?
* **Lê o catálogo local:** Puxa os dados de nome, preço, descrição, link e imagens do teu `produtos.csv`.
* **Trata duplicatas:** Remove automaticamente títulos repetidos para evitar o erro do Pinterest de *"Várias linhas com o mesmo título"*.
* **Limpa dados quebrados:** Ignora produtos que estejam sem link, sem imagem ou sem nome.
* **Formata limites:** Ajusta os tamanhos máximos permitidos pelo Pinterest (títulos até 100 caracteres e descrições até 500 caracteres).
* **Gera o feed pronto:** Cria o arquivo `feed_pinterest.csv` otimizado para o upload em massa.

---

## 🛠️ Como Usar

1. Certifica-te de que o arquivo `produtos.csv` está na mesma pasta do script com as colunas corretas (nome, preco, descricao, link, imagem/fotos).
2. Executa o script no terminal:
   ```bash
   py gerar_feed_pinterest.py
