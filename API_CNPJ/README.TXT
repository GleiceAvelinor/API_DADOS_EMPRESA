===========================================================
CONSULTA DE CNPJ VIA API - PYTHON
===========================================================

Este projeto é um script simples em Python que automatiza a 
consulta de dados cadastrais de empresas brasileiras utilizando 
a API pública do "CNPJ.ws".

---
1. PRÉ-REQUISITOS
---

Antes de rodar o script, você precisa ter o Python instalado 
em sua máquina e a biblioteca 'requests'.

Para instalar a biblioteca necessária, execute:
> pip install requests

---
2. COMO FUNCIONA
---

O script realiza as seguintes etapas:
1. Define o CNPJ que será consultado.
2. Monta a URL de consulta para a API publica.cnpj.ws.
3. Envia uma requisição HTTP GET.
4. Converte a resposta recebida para o formato JSON (Dicionário).
5. Exibe os dados completos da empresa no terminal.

---
3. COMO EXECUTAR
---

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta onde o arquivo está salvo.
3. Execute o comando:
   > python nome_do_seu_arquivo.py

---
4. OBSERVAÇÕES IMPORTANTES
---

* Limites de Uso: Verifique os limites da API gratuita em 
  https://www.cnpj.ws/ se planeja fazer muitas consultas.
* Erros de Conexão: Caso o CNPJ seja inválido ou a conexão 
  caia, o script pode retornar um erro. Recomenda-se tratar 
  esses casos em versões futuras.

---
Desenvolvido para fins de aprendizado e automação.(CURSO HASHTAG PROGRAMAÇÃO- PROF.LIRA)