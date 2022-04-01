# desafio_celero
API de 120 anos de olimpíadas, com informações sobre atletas e eventos.

### Como usar

**Primeiro inicie a API com o docker.**

`docker-compose build`

`docker-compose up`

**Acesse em `localhost:8000`**

As rotas são:

* **http://localhost:8000/api** - Rota raíz da API.
* **http://localhost:8000/api/athletes/** - Rota dos Atletas
* **http://localhost:8000/api/events/** - Rota dos Eventos
* **http://localhost:8000/api/games/** - Rota dos Jogos
* **http://localhost:8000/api/medals/** - Rota das Medalhas
* **http://localhost:8000/api/upload/** - Rota do upload do arquivo CSV.
