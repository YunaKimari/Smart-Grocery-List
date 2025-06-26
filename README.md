## Lista de Compras (lista_mercado) ![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
Um gerenciador de listas de compras de mercado com histórico de preços e manipulação de listas salvas.

## 🎮 Sobre o projeto
`lista_mercado` é uma aplicação de terminal desenvolvida em Python que permite criar, editar e reutilizar listas de compras. É idela para demonstrar conhecimentos em estruturação de projetos, manipulação de arquivos JSON,
reaproveitamento de código e boas práticas de programação.

## 🔧 Funcionalidades
- Criar nova lista de compras com título e local.
- Adicionar, editar e remover itens da lista.
- Salvar listas em arquivos locais com histórico.
- Duplicas listas existentes para novos usos.
- Ver menor preço já pago por item e sugestão de valor.
- Buscar listas por título.
- Validação de campos obrigatórios.
- Histórico automático de preços por item, data e local.

## 📁 Estrutura do projeto
- `app.py`: Arquivo principal que executa o programa.
- `models/`
  - `lista.py`: Classe da lista de compras.
  - `item.py`: Classe dos itens da lista.
- `controllers/`
  - `lista_controllers.py`: Gerencia operações principais com listas.
  - `lista_criacao.py`: Controla criação e inserção de itens.
- `services/`
  - `historico.py`: Serviço para lidar com histórico de preços.
  - `arquivo.py`: Serviço de leitura e escrita de arquivos.
- `config.py`: Contém constantes globais.
- `historico.json`: Armazena o histórico de preços.
- `listas_salvas/`: Pasta onde ficam as listas criadas pelo usuário.
- `README.md`: Este arquivo (em português e em inglês).

## 🚀 Como executar
- Python 3.10 ou superior.
- Terminal (Git Bash, CMD, PowerShell, etc.).

##### Passo 1. Clone o repositório:
```bash
git clone https://github.com/YunaKimari/lista_mercado.git
cd lista_mercado
```

##### Passo 2. Execute o programa:
```bash
python app.py
```

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.

## 👤 Autor
- YunaKimari (Denise Rocha)
- GitHub: github.com/YunaKimari

---

## Smart Grocery List (CLI) ![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
A command-line application in Python to manage your grocery lists efficiently, with price history, duplication, and item suggestions.

## 🎮 About th project
Smart Grocery List is a simple and smart Python CLI application designed to help users create, view, and manage grocery shopping lists. It offers advanced features like historical price tracking, item suggestions based on
previous data, and list duplication with edit options. It's ideal for those learning OOP, file handling, modular architecture, and terminal user interaction in Python.

## 🔧 Features
- Create grocery lists with title and store location.
- Add, update, or remove items (with quantity, unit, and notes).
- Suggest item prices based on purchase history.
- Show the lowest price ever paid for an item.
- Duplicate and edit old lists (remove/add new items).
- Save lists to JSON and automatically update price history.
- Load and search saved lists by title or date.

## 📁 Project structure
- `app.py`: Main entry point.
- `models/`
  - `lista.py`: Shopping list model.
  - `item.py`: Item model.
- `controllers/`
  - `lista_controllers.py`: CLI logic for loading, editing, duplicating.
  - `lista_criacao.py`: CLI logic for creating and updating lists.
- `services/`
  - `historico.py`: Price history functions.
  - `arquivo.py`: File reading/writing logic.
- `config.py`: Path constants.
- `historico.json`: Stored price history.
- `listas_salvas/`: Folder where JSON lists are stored.
- `README.md`: This file (in both Portuguese and English).

## 🚀 How to run
- Python 3.10+ required.
- Terminal (Git Bash, CMD, PowerShell, etc.).

##### Step 1. Clone the repository:
```bach
git clone https://github.com/YunaKimari/smart-grocery-list.git
cd lista_mercado
```

#### Step 2. Run the application:
```bash
python app.py
```

## 📄 License
This project is licenced under the MIT License.

## 👤 Author
- YunaKimari (Denise Rocha)
- GitHub: github.com/YunaKimari
