from fastapi import HTTPException

from database import db
from models.volunteer import CreateVolunteer
import repositories.volunteer as repo

def create_volunteer(vol: CreateVolunteer):
    if any(volunteer.email == vol.email for volunteer in db):
        raise HTTPException(
        status_code=400,
        detail="Email already exists"
    )
    return repo.add_volunteer(vol)
