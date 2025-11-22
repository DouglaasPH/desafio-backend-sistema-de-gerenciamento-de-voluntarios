from fastapi import HTTPException
from typing import List

from database import db
from models.volunteer import (
    Volunteer,
    CreateVolunteer,
    FiltersVolunteer,
    UpdateVolunteer,
)
import repositories.volunteer as repo


def create_volunteer(vol: CreateVolunteer) -> Volunteer:
    if any(volunteer.email == vol.email for volunteer in db):
        raise HTTPException(status_code=409, detail="O email pertence a um voluntário cadastrado.")
    return repo.add_volunteer(vol)


def list_volunteer(filters: FiltersVolunteer) -> List[Volunteer]:
    result = repo.filter_volunteer(filters)

    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Não encontrado.")
    else:
        return result


def get_volunteer(volunteer_id: int) -> Volunteer:
    result = repo.get_volunteer(volunteer_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Não encontrado.")
    else:
        return result


def update_volunteer(volunteer_id: int, data: UpdateVolunteer) -> Volunteer:
    result = repo.update_volunteer(volunteer_id, data)

    if result is None:
        raise HTTPException(status_code=404, detail="Voluntário não encontrado.")
    else:
        return result


def delete_volunteer(volunteer_id: int) -> Volunteer:
    result = repo.delete_volunteer(volunteer_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Voluntário não encontrado.")
    else:
        return result
