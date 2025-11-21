from fastapi import FastAPI

from routes.volunteer import router as volunteer_router

app = FastAPI(title="Sistema de Gerenciamento de Voluntários")

app.include_router(volunteer_router)
