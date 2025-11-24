import yaml

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.volunteer import router as volunteer_router

app = FastAPI(title="Sistema de Gerenciamento de Voluntários")


origins = [
    "https://sistema-de-gerenciamento-de-voluntarios.vercel.app/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ou ["*"] para liberar todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(volunteer_router)


with open("openapi.yaml", "r") as f:
    custom_openapi_yaml = yaml.safe_load(f)


def custom_openapi():
    return custom_openapi_yaml


app.openapi = custom_openapi
