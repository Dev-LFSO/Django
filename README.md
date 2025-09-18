# Django Project

Este repositório contém um projeto desenvolvido com o framework Django, utilizando Python.

## Funcionalidades

* Estrutura básica de um projeto Django.
* Arquivos de configuração essenciais para o desenvolvimento.
* Dependências listadas em `requirements.txt`.
* Arquivo `.gitignore` configurado para projetos Django.

## Tecnologias

* Python
* Django
* HTML, CSS, JavaScript

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Dev-LFSO/Django.git
```

2. Acesse a pasta do projeto:

```bash
cd Django
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # no Linux/macOS
venv\Scripts\activate     # no Windows
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

7. Acesse o projeto no navegador:

```
http://127.0.0.1:8000/
```

## Estrutura do Repositório

| Item               | Descrição                                    |
| ------------------ | -------------------------------------------- |
| `requirements.txt` | Lista de dependências necessárias            |
| `.gitignore`       | Arquivo para ignorar arquivos desnecessários |
| `design.txt`       | Documento com o design do projeto            |

## Licença

MIT License
