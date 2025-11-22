from datetime import datetime, UTC
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum


class StatusOptions(str, Enum):
    ativo = "Ativo"
    inativo = "Inativo"


class AvailabilityOptions(str, Enum):
    manha = "Manhã"
    tarde = "Tarde"
    noite = "Noite"


class Volunteer(BaseModel):
    id: int
    nome: str
    email: EmailStr
    cargo_pretendido: str
    disponibilidade: AvailabilityOptions
    status: StatusOptions = StatusOptions.ativo
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class CreateVolunteer(BaseModel):
    nome: str
    email: EmailStr
    cargo_pretendido: str
    disponibilidade: AvailabilityOptions


class UpdateVolunteer(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    cargo_pretendido: Optional[str] = None
    disponibilidade: Optional[AvailabilityOptions] = None


class FiltersVolunteer(BaseModel):
    status: Optional[StatusOptions] = None
    cargo_pretendido: Optional[str] = None
    disponibilidade: Optional[AvailabilityOptions] = None
