from fastapi import HTTPException
from typing import List

from database import db
from models.volunteer import Volunteer, CreateVolunteer, FiltersVolunteer
import repositories.volunteer as repo

def create_volunteer(vol: CreateVolunteer) -> Volunteer:
    if any(volunteer.email == vol.email for volunteer in db):
        raise HTTPException(
        status_code=400,
        detail="Email already exists"
    )
    return repo.add_volunteer(vol)


def list_volunteer(filters: FiltersVolunteer) -> List[Volunteer]:
    return repo.filter_volunteer(filters)