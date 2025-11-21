from fastapi import APIRouter
from typing import List, Optional

from models.volunteer import Volunteer, CreateVolunteer, FiltersVolunteer
import services.volunteer as service

router = APIRouter(prefix="", tags=["Volunteers"])

@router.post("/volunteer", response_model=Volunteer)
def create_volunteer(vol: CreateVolunteer):
    return service.create_volunteer(vol)


@router.get("/volunteer", response_model=List[Volunteer])
def list_volunteers(filters: Optional[FiltersVolunteer] = None):
    if filters is None:
        filters = FiltersVolunteer()
    return service.list_volunteer(filters)


@router.get("/volunteer/{volunteer_id}", response_model=Volunteer)
def get_volunteer(volunteer_id: int):
    return service.get_volunteer(volunteer_id)