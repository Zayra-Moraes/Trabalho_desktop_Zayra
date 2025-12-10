# Trabalho_desktop_Zayra
# CampManager - Gerenciador de Campeonatos

## 📋 Descrição
O **CampManager** é uma plataforma desenvolvida em **Python** para o gerenciamento completo de campeonatos esportivos. O projeto aplica princípios de **Programação Orientada a Objetos (POO)** e oferece duas interfaces de uso: uma via **Terminal (CLI)** e uma interface **Web** moderna construída com o framework **Bottle**.

O sistema permite o cadastro de jogadores, técnicos e equipes, a organização de campeonatos, criação de partidas e acompanhamento de tabelas de classificação com cálculo automático de pontos e saldo de gols.

---

##  Funcionalidades Principais:
- **Gerenciamento de Cadastros**:
  - Jogadores (com idade, CPF, posição).
  - Técnicos (com licença e equipe vinculada).
  - Equipes (com controle de ano de fundação e integrantes).
  - Campeonatos.
- **Gestão de Partidas**:
  - Criação de partidas entre equipes inscritas.
  - Registro de placares (ex: "2x1").
  - Definição automática de vencedor ou empate.
- **Classificação**:
  - Tabela de pontos e saldo de gols atualizada automaticamente após cada partida.
- **Persistência de Dados**:
  - Todos os dados são salvos em arquivos JSON, garantindo que as informações não sejam perdidas ao fechar a aplicação.

---
## Tecnologias Utilizadas

- **Linguagem**: Python 3.13
- **Web Framework**: Bottle
- **Front-end**: HTML, CSS, Bootstrap 5 (Templates `.tpl`)
- **Armazenamento**: JSON (File-based storage)
--- 

## 📂 Estrutura de Arquivos

O projeto está organizado em pacotes para separar responsabilidades:

- `package/controllers/`: Lógica de controle e gerenciamento de dados.
  - `data/`: Arquivos JSON onde os dados são persistidos.
  - `menu/`: Lógica dos menus para a versão CLI.
- `package/models/`: Classes principais do domínio (Jogador, Equipe, Campeonato, Partida, etc.).
- `package/views/`: Templates HTML para a interface Web.
- `package/static/`: Arquivos estáticos (CSS, Imagens).
- `app.py`: Ponto de entrada para a **Interface Web**.
- `main.py`: Ponto de entrada para a **Interface CLI (Terminal)**.
---


### Pré-requisitos
``` markdown
O projeto utiliza o framework `bottle` para a interface web. Instale-o com:
bash pip install bottle
```



### 1. Interface Web
Para iniciar a aplicação web, execute o arquivo `app.py`:
```

bash python app.py
Em seguida, acesse no seu navegador: `http://127.0.0.1:8080/`
```
### 2. Interface Terminal (CLI)
``` 

Para utilizar o sistema via linha de comando com menus interativos, execute o arquivo `main.py`:
bash python main.py
```


## link do vídeo mostrando as funcionalidades: https://drive.google.com/file/d/1fH9FrVVuP8uFgUnK7zKTCFPJV7EjBfgc/view?usp=sharing