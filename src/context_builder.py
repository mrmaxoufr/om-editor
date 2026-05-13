from datetime import date


def format_date(value: date) -> str:
    """Format a Python date object using the French date format.

    Parameters
    ----------
    value:
        Date object to format.

    Returns
    -------
    str
        Date formatted as `dd/mm/YYYY`.
    """
    return value.strftime("%d/%m/%Y")


def empty_trajet(prefix: str, index: int) -> dict[str, str]:
    """Create an empty trip dictionary for template completion.

    This function is used to automatically fill unused lines in Word
    templates so that all expected variables exist.

    Parameters
    ----------
    prefix:
        Prefix used in template variables (`aller`, `retour`, `perso`).
    index:
        Trip line index.

    Returns
    -------
    dict[str, str]
        Dictionary containing empty values for a trip line.
    """
    return {
        f"{prefix}_{index}_depart_ville": "",
        f"{prefix}_{index}_date_depart": "",
        f"{prefix}_{index}_heure_depart": "",
        f"{prefix}_{index}_arrivee_ville": "",
        f"{prefix}_{index}_date_arrivee": "",
        f"{prefix}_{index}_heure_arrivee": "",
    }


def complete_trajets(
    trajets: list[dict[str, str]],
    prefix: str,
    max_count: int,
) -> list[dict[str, str]]:
    """Complete a trip list with empty entries until a maximum size.

    Word templates expect a fixed number of variables. This helper ensures
    that all required variables exist even if the user entered fewer trips.

    Parameters
    ----------
    trajets:
        List of existing trip dictionaries.
    prefix:
        Prefix used in template variables.
    max_count:
        Maximum number of trip lines expected by the template.

    Returns
    -------
    list[dict[str, str]]
        Completed list of trip dictionaries.
    """
    completed = trajets.copy()

    for index in range(len(completed) + 1, max_count + 1):
        completed.append(empty_trajet(prefix, index))

    return completed


def build_context(
    missionnaire: dict,
    mission: dict,
    signature: dict,
    trajets: list[dict[str, str]],
    vehicle: dict | None = None,
    subscription: dict | None = None,
) -> dict:
    """Build the rendering context for the DOCX template.

    This function centralizes all values passed to the Word template and
    merges:
    - missionnaire information;
    - mission information;
    - trip information;
    - vehicle information;
    - subscription card information.

    Parameters
    ----------
    missionnaire:
        Dictionary containing missionnaire information.
    mission:
        Dictionary containing mission details.
    signature:
        Dictionary containing signature information.
    trajets:
        List of trip dictionaries.
    vehicle:
        Optional vehicle-related information.
    subscription:
        Optional transport subscription information.

    Returns
    -------
    dict
        Final rendering context used by `docxtpl`.
    """
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

    vehicle = vehicle or {}
    subscription = subscription or {}

    context.update(
        {
            "type_vehicule": vehicle.get("type_vehicule", ""),
            "motif_vehicule": vehicle.get("motif_vehicule", ""),
            "kilometrage_vehicule": vehicle.get(
                "kilometrage_vehicule",
                "",
            ),
            "immatriculation_vehicule": vehicle.get(
                "immatriculation_vehicule",
                "",
            ),
            "nom_carte_abonnement": subscription.get(
                "nom_carte_abonnement",
                "",
            ),
            "numero_carte_abonnement": subscription.get(
                "numero_carte_abonnement",
                "",
            ),
            "debut_validite_carte_abonnement": subscription.get(
                "debut_validite_carte_abonnement",
                "",
            ),
            "fin_validite_carte_abonnement": subscription.get(
                "fin_validite_carte_abonnement",
                "",
            ),
        }
    )

    return context