from pathlib import Path

import yaml


def load_profiles(path: Path) -> dict:
    """Load missionnaire profiles from a YAML file.

    If the file does not exist, an empty dictionary is returned. This allows
    the application to run even when the local `data/profils.yaml` file has
    not been created yet.

    Parameters
    ----------
    path:
        Path to the YAML file containing user profiles.

    Returns
    -------
    dict
        Dictionary of available profiles.
    """
    if not path.exists():
        return {}

    with open(path, encoding="utf-8") as file:
        return yaml.safe_load(file) or {}