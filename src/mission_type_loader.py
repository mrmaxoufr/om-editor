from pathlib import Path

import yaml


def load_mission_types(path: Path) -> dict:
    """Load mission type presets from a YAML file.

    If the file does not exist, an empty dictionary is returned. This allows
    users to run the application without predefined mission types.

    Parameters
    ----------
    path:
        Path to the YAML file containing mission type presets.

    Returns
    -------
    dict
        Dictionary of available mission type presets.
    """
    if not path.exists():
        return {}

    with open(path, encoding="utf-8") as file:
        return yaml.safe_load(file) or {}