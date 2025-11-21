from typing import List
from database import db
from models.volunteer import Volunteer, CreateVolunteer, FiltersVolunteer

def add_volunteer(vol: CreateVolunteer) -> Volunteer:
    new_volunteer = Volunteer(
        id=len(db) + 1,
        nome= vol.nome,
        email= vol.email,
        cargo_pretendido=vol.cargo_pretendido,
        disponibilidade=vol.disponibilidade
        
    )
    db.append(new_volunteer)
    return new_volunteer


def filter_volunteer(filters: FiltersVolunteer) -> List[Volunteer]:
    results = []
    
    for volunteer in db:
        if filters.status is not None and volunteer.status != filters.status:
            continue
        
        if filters.cargo_pretendido is not None and volunteer.cargo_pretendido != filters.cargo_pretendido:
            continue
        
        if filters.disponibilidade is not None and volunteer.disponibilidade != filters.disponibilidade:
            continue
        
        results.append(volunteer)
    
    return results