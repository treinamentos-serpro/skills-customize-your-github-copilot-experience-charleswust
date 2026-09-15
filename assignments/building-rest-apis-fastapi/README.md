# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar um catálogo de livros usando o framework FastAPI, modelos Pydantic, rotas HTTP e códigos de status apropriados.

## 📝 Tasks

### 🛠️ Criar e explorar a API

#### Descrição
Execute o starter code, complete a rota inicial e crie um endpoint que retorne todos os livros do catálogo em formato JSON.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` com um título descritivo
- Disponibilizar uma rota `GET /` que retorne uma mensagem de boas-vindas
- Disponibilizar uma rota `GET /books` que retorne a lista completa de livros
- Iniciar o servidor com `uvicorn starter-code:app --reload` e permitir testes pela documentação interativa em `/docs`


### 🛠️ Adicionar e consultar livros

#### Descrição
Use um modelo Pydantic para validar novos livros e implemente rotas para adicionar um livro e consultar um livro específico pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Definir um modelo `BookCreate` com título, autor e ano de publicação
- Disponibilizar uma rota `POST /books` que valide o corpo da requisição e crie um identificador único
- Retornar o livro criado com código de status `201`
- Disponibilizar uma rota `GET /books/{book_id}` que retorne um livro existente
- Retornar código `404` quando o identificador solicitado não existir

Exemplo de requisição para `POST /books`:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "published_year": 1937
}
```


### 🛠️ Atualizar e remover livros

#### Descrição
Complete a API com operações de atualização e remoção para que o catálogo suporte o ciclo CRUD completo.

#### Requisitos
O programa concluído deve:

- Disponibilizar uma rota `PUT /books/{book_id}` para substituir os dados de um livro existente
- Validar os dados recebidos antes de atualizar o catálogo
- Disponibilizar uma rota `DELETE /books/{book_id}` para remover um livro existente
- Retornar código `404` para atualizações ou remoções de identificadores inexistentes
- Retornar uma resposta JSON clara e um código de status apropriado após cada operação
