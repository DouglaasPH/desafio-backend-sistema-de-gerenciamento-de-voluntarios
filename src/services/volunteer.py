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
    result = repo.filter_volunteer(filters)
    
    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Not found") 
    else:
        return result

def get_volunteer(volunteer_id: int) -> Volunteer:
    result = repo.get_volunteer(volunteer_id)
    
    if result == {}:
        raise HTTPException(status_code=404, detail="Not found") 
    else:
        return result