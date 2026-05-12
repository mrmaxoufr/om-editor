from datetime import date


def format_date(value: date) -> str:
    return value.strftime("%d/%m/%Y")


def build_context(
    missionnaire: dict,
    mission: dict,
    signature: dict,
    trajets: list[dict[str, str]],
) -> dict:
    context = {
        "nom": missionnaire["nom"],
        "prenom": missionnaire["prenom"],
        "date_naissance": format_date(missionnaire["date_naissance"]),
        "mail": missionnaire["mail"],
        "telephone": missionnaire["telephone"],
        "adresse": missionnaire["adresse"],
        "code_postal": missionnaire["code_postal"],
        "ville": missionnaire["ville"],
        "nationalite": missionnaire["nationalite"],
        "profession": missionnaire["profession"],
        "motif_mission": mission["motif_mission"],
        "date_depart_residence": format_date(
            mission["date_depart_residence"]
        ),
        "date_retour_residence": format_date(
            mission["date_retour_residence"]
        ),
        "fait_a": signature["fait_a"],
        "date_signature": format_date(signature["date_signature"]),
    }

    for trajet in trajets:
        context.update(trajet)

    return context