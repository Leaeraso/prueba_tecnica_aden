from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
import app.models

from app.routers import students, courses, enrollments, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(students.router, prefix="/api/v1")
app.include_router(courses.router, prefix="/api/v1")
app.include_router(enrollments.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.app_name}"}
