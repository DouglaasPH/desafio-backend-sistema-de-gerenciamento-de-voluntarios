from pydantic import BaseModel, EmailStr
from enum import Enum

class OpcoesDeDisponibilidade(str, Enum):
    manha = "manhã"
    tarde = "tarde"
    noite = "noite"

class Voluntarios(BaseModel):
    id: int
    nome: str
    email: EmailStr
    cargo_pretendido: str
    disponibilidade: OpcoesDeDisponibilidade
    status: str