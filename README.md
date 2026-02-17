# SubTrack APP 🚀

A professional subscription management ecosystem built with a focus on scalability, security, and clean architecture.

## 📌 Overview

SubTrack is a high-performance API designed to manage service subscriptions, track recurring payments, and provide insights into user expenses. This project follows the **Clean Architecture** principles to ensure maintainability and testability.

## 🛠 Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.12+)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLModel](https://sqlmodel.tiangolo.com/) (Pydantic + SQLAlchemy integration)
- **Cache & Rate Limiting:** [Redis](https://redis.io/)
- **Security:** OAuth2 with JWT (Stateless) and Argon2 hashing.
- **Infrastructure:** Docker & Docker Compose.
- **Quality Assurance:** Pytest (Testing) and Ruff (Linting/Formatting).

## 🏗 Architecture

The project is structured into layers to separate concerns:

- **Routes:** Entry points for API requests.
- **Services:** Core business logic and rules.
- **Models:** Database definitions (SQLModel).
- **Repositories:** Data access abstraction.
- **Middlewares:** Global request logging, CORS, and standardized Error Handling.

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed.
- Python 3.12+ (for local development).

---

### 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/lucasdamasceno96/subtrack-app.git
cd subtrack-app

```

2. **Setup environment variables:**

```bash
cp .env.example .env

```

3. **Run the application with Docker:**

```bash
docker-compose up --build

```

A aplicação estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa (Swagger UI) em `http://localhost:8000/docs`.

---

## 📜 Development Guidelines

Para manter a consistência do projeto, siga estas diretrizes:

- **Commits:** Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/).
- **Language:** Todo o código, variáveis e comentários devem ser em **Inglês**.
- **Linting:** Execute `ruff check .` antes de realizar o commit.
- **Testing:** Utilize `pytest` para garantir que todas as funcionalidades estão operando corretamente.

---

_Developed as a part of a deep-learning journey in Backend Engineering._

---
