# Escola REST API
A Escola REST API é uma aplicação que oferece funcionalidades através de uma API RESTful. Ela permite a comunicação entre plataformas e a reutilização de funcionalidades. Aqui estão algumas informações relevantes:

# Tecnologias Utilizadas
**Django**: Um framework web em Python que facilita o desenvolvimento rápido e escalável de aplicações.
**Django REST Framework**: Uma extensão do Django que simplifica a criação de APIs RESTful.
**Banco de Dados SQLite**: Utilizado para armazenar dados da aplicação.
**Redis**: Banco de dados local para armazenar o cache do servidor.

**Como Executar o Projeto**
Clone o repositório: git clone https://github.com/dnsouzadev/escola-rest-api.git

Instale as dependências: pip install -r requirements.txt

Execute as migrações do banco de dados: python manage.py migrate

Inicie o servidor: python manage.py runserver

Acesse a API em http://localhost:8000/ e explore os endpoints disponíveis!
