# University Module — Odoo 17

Módulo de gestión académica universitaria desarrollado con **Odoo 17** como parte de una prueba técnica. Permite administrar estudiantes, profesores, carreras, planes de estudio, inscripciones y aulas.

## Requisitos

- Docker y Docker Compose
- Python 3.10+ (solo para desarrollo local)

## Instalación y ejecución

### Con Docker (recomendado)

```bash
docker-compose up -d
```

Esto levanta dos servicios:
- **PostgreSQL 15** en el contenedor `odoo_db`
- **Odoo 17** en el contenedor `odoo_app`, accesible en `http://localhost:8069`

### Instalar el módulo

1. Acceder a `http://localhost:8069`
2. Crear una base de datos (usuario admin, contraseña admin)
3. Activar modo desarrollador: `Settings > General Settings > Developer Tools`
4. Ir a `Apps > Update Apps List`
5. Buscar **University** e instalar

## Estructura del módulo

```
addons/university/
├── models/
│   ├── student.py
│   ├── professor.py
│   ├── career.py
│   ├── subject.py
│   ├── grade.py
│   ├── student_status.py
│   ├── study_plan.py
│   ├── subject_study_plan.py
│   ├── enrollment.py
│   ├── classroom.py
│   └── enrollment_subject_classroom.py
├── views/
│   ├── student_views.xml
│   ├── professor_views.xml
│   ├── career_views.xml
│   ├── subject_views.xml
│   ├── grade_views.xml
│   ├── student_status_views.xml
│   ├── study_plan_views.xml
│   ├── enrollment_views.xml
│   ├── classroom_views.xml
│   └── menu.xml
├── security/
│   ├── groups.xml
│   └── ir.model.access.csv
├── __init__.py
└── __manifest__.py
```

## Modelos

| Modelo | Descripción |
|--------|-------------|
| `university.student` | Estudiantes con número autogenerado (desde 50000) |
| `university.professor` | Profesores con número autogenerado (desde 1000) |
| `university.career` | Carreras universitarias |
| `university.subject` | Materias |
| `university.grade` | Años/niveles académicos |
| `university.student_status` | Estados del estudiante (activo, egresado, etc.) |
| `university.study_plan` | Planes de estudio vinculados a una carrera |
| `university.subject_study_plan` | Relación materia–año dentro de un plan de estudio |
| `university.enrollment` | Inscripción de un estudiante a una carrera/plan |
| `university.classroom` | Aulas con capacidad definida |
| `university.enrollment_subject_classroom` | Asignación de materia y aula dentro de una inscripción |

## Roles y permisos

| Grupo | Acceso |
|-------|--------|
| **Academic** | CRUD completo sobre todos los modelos |
| **Finance** | Solo lectura sobre el modelo de Profesores |

El menú principal **University** es visible para ambos grupos. El submenú de Configuración es exclusivo del grupo Academic.

## Dependencias de desarrollo

```bash
pip install -r requirements.txt
```

Incluye: `pylint-odoo`, `flake8`, `black`, `isort`, `pytest-odoo`, `pre-commit`.
