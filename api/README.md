# University API

REST API para gestión de inscripciones universitarias. Permite crear estudiantes, cursos y gestionar inscripciones a carreras y materias.

## Tecnologías

- **FastAPI** — framework web
- **SQLAlchemy** — ORM
- **PostgreSQL** — base de datos
- **Pydantic v2** — validación y serialización
- **JWT (python-jose)** — autenticación
- **Docker + pgAdmin** — infraestructura local

## Requisitos

- Python 3.11+
- Docker y Docker Compose

## Instalación y uso

### 1. Levantar la base de datos

```bash
docker-compose up -d
```

Esto levanta:
- PostgreSQL en `localhost:5432`
- pgAdmin en `http://localhost:5050` (usuario: `admin@admin.com` / contraseña: `admin`)

### 2. Crear el entorno virtual e instalar dependencias

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql://admin:admin@localhost:5432/university_db
SECRET_KEY=cambia-esto-en-produccion-por-algo-largo-y-aleatorio
ALGORITHM=HS256
EXPIRES_IN=3600
APP_NAME=University API
DEBUG=true
STUDENT_NUMBER_START=50000
CLASSROOM_NUMBER_START=100
```

### 4. Levantar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.
Documentación interactiva: `http://localhost:8000/docs`

---

## Endpoints

### Auth

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/api/v1/auth/login` | Login, devuelve JWT | No |

**Body:**
```json
{
  "email": "estudiante@mail.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

---

### Students

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/api/v1/students` | Crear estudiante | No |

**Body:**
```json
{
  "name": "Juan",
  "last_name": "Pérez",
  "email": "juan@mail.com",
  "password": "password123",
  "dni": 12345678,
  "date_of_birth": "2000-01-15"
}
```

> `student_number` y `status` se asignan automáticamente.

---

### Courses

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/api/v1/courses` | Crear aula/curso | No |

**Body:**
```json
{
  "capacity": 30
}
```

> `classroom_number` se asigna automáticamente.

---

### Enrollments

Todos los endpoints requieren autenticación. Incluir header:
```
Authorization: Bearer <token>
```

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/enrollments` | Inscribir estudiante a una carrera |
| POST | `/api/v1/enrollments/{enrollment_id}/subjects` | Inscribir a una materia |
| GET | `/api/v1/enrollments/student/{student_id}` | Listar inscripciones de un estudiante |

**Inscripción a carrera — body:**
```json
{
  "student_id": 1,
  "career_id": 1,
  "study_plan_id": 1
}
```

**Inscripción a materia — body:**
```json
{
  "subject_study_plan_id": 1,
  "classroom_id": 1
}
```

---

## Reglas de negocio

- No se permiten inscripciones duplicadas (misma carrera o misma materia).
- Un aula tiene capacidad máxima. El límite se valida por `aula + materia` (la misma aula puede usarse para distintas materias).
- El `study_plan` debe pertenecer a la `career` indicada al inscribir.
- Al crear un estudiante, su estado se asigna automáticamente como `active`.

---

## Estructura del proyecto

```
app/
├── core/
│   ├── config.py          # Variables de entorno (pydantic-settings)
│   ├── database.py        # Engine y sesión de SQLAlchemy
│   ├── security.py        # Hash de contraseñas y JWT
│   ├── dependencies.py    # get_current_user, require_role
│   └── exceptions.py      # Excepciones HTTP reutilizables
├── models/                # Modelos SQLAlchemy
├── repositories/          # Acceso a datos (queries)
├── services/              # Lógica de negocio
├── schemas/               # Schemas Pydantic (request/response)
└── routers/               # Endpoints FastAPI
```

## Autenticación

La API usa **JWT Bearer tokens**. Para usar endpoints protegidos:

1. Hacer `POST /api/v1/auth/login` con email y password.
2. Copiar el `access_token` de la respuesta.
3. En `/docs`, hacer click en **Authorize** e ingresar el token.
