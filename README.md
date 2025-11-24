# Desafio Backend - Sistema de Gerenciamento de Voluntários

Projeto desenvolvido em **FastAPI** para gerenciar voluntários, incluindo criação, listagem, atualização e exclusão.

---

## Requisitos

- Python >=3.13,<4.0
- Poetry

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/DouglaasPH/desafio-backend-sistema-de-gerenciamento-de-voluntarios.git
cd desafio-backend-sistema-de-gerenciamento-de-voluntarios
```

2. Instale as dependências com Poetry:

```bash
poetry install
```

3. Ative o ambiente virtual do Poetry:

```bash
poetry shell
```

---

## Execução

Para executar a aplicação localmente:

```bash
poetry run task run
```

A aplicação estará disponível em `http://127.0.0.1:8000` com **hot reload**.  
A documentação interativa do Swagger pode ser acessada em `http://127.0.0.1:8000/docs`.

---

## Rotas da API

| Método | Endpoint                    | Descrição                                  |
| ------ | --------------------------- | ------------------------------------------ |
| POST   | `/volunteer`                | Cria um novo voluntário                    |
| GET    | `/volunteer`                | Lista voluntários (opcional com filtros)   |
| GET    | `/volunteer/{volunteer_id}` | Retorna um voluntário com base no ID       |
| PUT    | `/volunteer/{volunteer_id}` | Atualiza dados de um voluntário existente  |
| DELETE | `/volunteer/{volunteer_id}` | Remove (soft delete) um voluntário pelo ID |

**Filtros opcionais para listagem** (`FiltersVolunteer`):

- `status`: `True` ou `False`
- `disponibilidade`: `manha`, `tarde`, `noite`
- `cargo_pretendido`: `nome_do_cargo`

---

## Testes

Para executar os testes:

```bash
poetry run task test
```

---

## Linting

Para verificar o estilo do código com **flake8**:

```bash
poetry run task lint
```

O projeto segue o padrão de **79 caracteres por linha** conforme configuração do Black e flake8.

---

## Formatação automática

Para formatar o código automaticamente com **Black**:

```bash
poetry run task format
```

---

## Observações

- O projeto utiliza **Taskipy** para facilitar execução de tarefas (`run`, `test`, `lint`, `format`).
- O banco de dados utilizado é um simples **array em memória** (`db`), para fins de teste.
