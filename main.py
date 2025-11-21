import yaml
from fastapi import FastAPI

from routes.volunteer import router as volunteer_router

app = FastAPI(title="Sistema de Gerenciamento de Voluntários")

app.include_router(volunteer_router)


with open("openapi.yaml", "r") as f:
    custom_openapi_yaml = yaml.safe_load(f)


def custom_openapi():
    return custom_openapi_yaml


app.openapi = custom_openapi
