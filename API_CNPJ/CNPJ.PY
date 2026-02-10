import requests

cnpj = "06947283000160,"

url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

requisicao = requests.get(url)
dados = requisicao.json()
print(dados)



