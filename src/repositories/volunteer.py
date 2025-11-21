from datetime import datetime

from database import db
from models.volunteer import CreateVolunteer, Volunteer

def add_volunteer(vol: CreateVolunteer):
    new_volunteer = Volunteer(
        id=len(db) + 1,
        nome= vol.nome,
        email= vol.email,
        cargo_pretendido=vol.cargo_pretendido,
        disponibilidade=vol.disponibilidade
        
    )
    db.append(new_volunteer)
    return new_volunteer