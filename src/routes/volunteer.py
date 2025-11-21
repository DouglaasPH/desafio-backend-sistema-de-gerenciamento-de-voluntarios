from fastapi import APIRouter, HTTPException
from typing import List

from models.volunteer import Volunteer, CreateVolunteer, FiltersVolunteer
import services.volunteer as service

router = APIRouter(prefix="", tags=["Volunteers"])

@router.post("/volunteer", response_model=Volunteer)
def create_volunteer(vol: CreateVolunteer):
    return service.create_volunteer(vol)


@router.get("/volunteer", response_model=List[Volunteer])
def list_volunteers(filters: FiltersVolunteer):
    return service.list_volunteer(filters)