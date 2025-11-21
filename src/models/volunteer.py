from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class OpcoesDeDisponibilidade(str, Enum):
    manha = "manha"
    tarde = "tarde"
    noite = "noite"

class Volunteer(BaseModel):
    id: int
    nome: str
    email: EmailStr
    cargo_pretendido: str
    disponibilidade: OpcoesDeDisponibilidade
    status: bool = True
    created_at: datetime = datetime.now()
    

class CreateVolunteer(BaseModel):
    nome: str
    email: EmailStr
    cargo_pretendido: str
    disponibilidade: OpcoesDeDisponibilidade
    

class UpdateVolunteer(BaseModel):
    id: Optional[int]
    nome: Optional[str]
    email: Optional[EmailStr]
    cargo_pretendido: Optional[str]
    disponibilidade: Optional[OpcoesDeDisponibilidade]    


class FiltersVolunteer(BaseModel):
    cargo_pretendido: Optional[str]
    disponibilidade: Optional[OpcoesDeDisponibilidade]
