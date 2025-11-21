from fastapi import APIRouter, HTTPException
from typing import List, Optional

from models.volunteer import (
    Volunteer,
    CreateVolunteer,
    FiltersVolunteer,
    UpdateVolunteer
)
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


@router.put("/volunteer/{volunteer_id}", response_model=Volunteer)
def update_volunteer(
    volunteer_id: int,
    data: Optional[UpdateVolunteer] = None
):
    if (
        data is None
        or (
            data.nome is None
            and data.email is None
            and data.cargo_pretendido is None
            and data.disponibilidade is None
        )
    ):
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    return service.update_volunteer(volunteer_id, data)


@router.delete("/volunteer/{volunteer_id}", response_model=Volunteer)
def delete_volunteer(volunteer_id: int):
    return service.delete_volunteer(volunteer_id)
