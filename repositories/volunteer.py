from typing import List
from database import db
from models.volunteer import (
    Volunteer,
    CreateVolunteer,
    FiltersVolunteer,
    UpdateVolunteer,
    StatusOptions
)


def add_volunteer(vol: CreateVolunteer) -> Volunteer:
    new_volunteer = Volunteer(
        id=len(db) + 1,
        nome=vol.nome,
        email=vol.email,
        cargo_pretendido=vol.cargo_pretendido,
        disponibilidade=vol.disponibilidade,
    )
    db.append(new_volunteer)
    return new_volunteer


def filter_volunteer(filters: FiltersVolunteer) -> List[Volunteer]:
    results = []

    for volunteer in db:
        if filters.status is not None and volunteer.status != filters.status:
            continue

        if (
            filters.cargo_pretendido is not None
            and volunteer.cargo_pretendido != filters.cargo_pretendido
        ):
            continue

        if (
            filters.disponibilidade is not None
            and volunteer.disponibilidade != filters.disponibilidade
        ):
            continue

        results.append(volunteer)

    return results


def get_volunteer(volunteer_id: int) -> Volunteer | None:
    for volunteer in db:
        if volunteer.id == volunteer_id:
            return volunteer
    return None


def update_volunteer(volunteer_id: int, data: UpdateVolunteer) -> Volunteer:
    volunteer = get_volunteer(volunteer_id)

    if volunteer is None:
        return volunteer

    volunteer.nome = data.nome if data.nome is not None else volunteer.nome
    volunteer.email = data.email if data.email is not None else volunteer.email
    volunteer.cargo_pretendido = (
        data.cargo_pretendido
        if data.cargo_pretendido is not None
        else volunteer.cargo_pretendido
    )
    volunteer.disponibilidade = (
        data.disponibilidade
        if data.disponibilidade is not None
        else volunteer.disponibilidade
    )

    db[volunteer_id - 1] = volunteer

    return volunteer


def delete_volunteer(volunteer_id: int) -> Volunteer:
    volunteer = get_volunteer(volunteer_id)

    if volunteer is None:
        return volunteer

    volunteer.status = StatusOptions.inativo

    db[volunteer_id - 1] = volunteer

    return volunteer
