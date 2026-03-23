# Prueba Técnica — Desarrollador Backend JR

Solución completa a la prueba técnica para el puesto de Desarrollador Backend JR en ADEN. El proyecto está dividido en dos partes independientes: una API REST con FastAPI y un módulo de gestión académica en Odoo 17.

---

## Estructura del repositorio

```
prueba-tecnica-aden/
├── api/        # API REST universitaria (FastAPI + PostgreSQL)
└── odoo/       # Módulo universitario (Odoo 17)
```

---

## Parte 1 — API REST (FastAPI)

API REST para la gestión de inscripciones universitarias. Permite crear estudiantes y aulas, autenticar usuarios con JWT, e inscribir estudiantes a carreras y materias.

### Tecnologías

- **FastAPI** — framework web
- **SQLAlchemy** — ORM
- **PostgreSQL** — base de datos
- **Pydantic v2** — validación y serialización
- **JWT (python-jose)** — autenticación
- **Docker + pgAdmin** — infraestructura local

### Puesta en marcha

```bash
# 1. Levantar base de datos
cd api
docker-compose up -d

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt

# 3. Crear archivo .env con las variables necesarias
# Ver api/README.md para el contenido completo

# 4. Levantar el servidor
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.
Documentación interactiva: `http://localhost:8000/docs`

### Endpoints principales

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/api/v1/auth/login` | Login, devuelve JWT | No |
| POST | `/api/v1/students` | Crear estudiante | No |
| POST | `/api/v1/courses` | Crear aula/curso | No |
| POST | `/api/v1/enrollments` | Inscribir a una carrera | Sí |
| POST | `/api/v1/enrollments/{id}/subjects` | Inscribir a una materia | Sí |
| GET | `/api/v1/enrollments/student/{id}` | Ver inscripciones del estudiante | Sí |

> Ver [`api/README.md`](./api/README.md) para documentación completa de endpoints, body y respuestas.

---

## Parte 2 — Módulo Odoo 17

Módulo de gestión académica universitaria desarrollado sobre Odoo 17. Administra estudiantes, profesores, carreras, planes de estudio, inscripciones y aulas desde una interfaz web.

### Tecnologías

- **Odoo 17**
- **PostgreSQL 15**
- **Docker + Docker Compose**

### Puesta en marcha

```bash
cd odoo
docker-compose up -d
```

Esto levanta:
- **PostgreSQL 15** en el contenedor `odoo_db`
- **Odoo 17** en `http://localhost:8069`

Luego instalar el módulo:
1. Acceder a `http://localhost:8069` y crear una base de datos
2. Activar modo desarrollador: `Settings > General Settings > Developer Tools`
3. Ir a `Apps > Update Apps List`
4. Buscar **University** e instalar

### Modelos implementados

| Modelo | Descripción |
|--------|-------------|
| `university.student` | Estudiantes con número autogenerado (desde 50000) |
| `university.professor` | Profesores con número autogenerado (desde 1000) |
| `university.career` | Carreras universitarias |
| `university.subject` | Materias |
| `university.grade` | Años/niveles académicos |
| `university.student_status` | Estados del estudiante |
| `university.study_plan` | Planes de estudio vinculados a una carrera |
| `university.subject_study_plan` | Relación materia–año dentro de un plan |
| `university.enrollment` | Inscripción de un estudiante a una carrera/plan |
| `university.classroom` | Aulas con capacidad definida |
| `university.enrollment_subject_classroom` | Asignación de materia y aula en una inscripción |

### Roles y permisos

| Grupo | Acceso |
|-------|--------|
| **Academic** | CRUD completo sobre todos los modelos |
| **Finance** | Solo lectura sobre el modelo de Profesores |

> Ver [`odoo/README.md`](./odoo/README.md) para instrucciones detalladas.

---

## Reglas de negocio compartidas

- No se permiten inscripciones duplicadas (misma carrera o misma materia).
- Un aula tiene capacidad máxima validada por aula + materia.
- El plan de estudio debe pertenecer a la carrera indicada al inscribir.
- Al crear un estudiante, su estado se asigna automáticamente como `active`.
