# API DADOS EMPRESA 🏢

## 📝 Descrição

Script em Python que automatiza a consulta de dados cadastrais de empresas brasileiras utilizando a API pública do **CNPJ.ws**. Facilita a busca e integração de informações de CNPJ de forma simples e eficiente.

## 🛠️ Tecnologias

- **Python** 3.8+
- **Requests** - Para requisições HTTP
- **CNPJ.ws API** - Fonte de dados

## 📂 Estrutura do Projeto

```
API_DADOS_EMPRESA/
├── README.md              # Documentação principal
├── .gitignore             # Arquivos ignorados pelo Git
├── .editorconfig          # Configuração do editor
├── requirements.txt       # Dependências do projeto
├── LICENSE                # Licença do projeto
│
├── src/                   # Código fonte
│   ├── __init__.py
│   └── consultar_cnpj.py  # Script principal
│
├── tests/                 # Testes
│   ├── __init__.py
│   └── test_consulta.py
│
└── docs/                  # Documentação adicional
    └── GUIA_USO.md
```

## 🚀 Como Usar

### 1. Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes)

### 2. Instalação

```bash
# Clone o repositório
git clone https://github.com/GleiceAvelinor/API_DADOS_EMPRESA.git
cd API_DADOS_EMPRESA

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows
venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Uso

```python
from src.consultar_cnpj import ConsultarCNPJ

consulta = ConsultarCNPJ()
dados = consulta.buscar("11222333000181")
print(dados)
```

## 📊 Exemplos de Resposta

```json
{
  "cnpj": "11222333000181",
  "nome": "Empresa Exemplo LTDA",
  "status": "Ativa",
  "data_abertura": "2020-01-15"
}
```

## 🧪 Testes

```bash
# Executar testes
python -m pytest tests/

# Com cobertura
pytest --cov=src tests/
```

## 📚 Documentação Adicional

Veja [GUIA_USO.md](docs/GUIA_USO.md) para mais detalhes.

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**Gleice Avelino**
- GitHub: [@GleiceAvelinor](https://github.com/GleiceAvelinor)

## 📞 Suporte

Se encontrar problemas, abra uma [issue](https://github.com/GleiceAvelinor/API_DADOS_EMPRESA/issues).

---

⭐ Se este projeto foi útil, considere dar uma estrela!
