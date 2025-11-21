from fastapi import APIRouter, HTTPException

from models.volunteer import CreateVolunteer, Volunteer
import services.volunteer as service

router = APIRouter(prefix="", tags=["Volunteers"])

@router.post("/volunteer", response_model=Volunteer)
def create_volunteer(vol: CreateVolunteer):
    return service.create_volunteer(vol)
