from pathlib import Path

from docxtpl import DocxTemplate


def render_ordre_mission(
    template_path: Path,
    output_path: Path,
    context: dict,
) -> None:
    """Generate an ordre de mission DOCX from a Word template.

    Parameters
    ----------
    template_path:
        Path to the `.docx` template containing Jinja-style variables.
    output_path:
        Path where the generated document should be saved.
    context:
        Dictionary containing the values used to replace the template
        variables.

    Returns
    -------
    None
    """
    doc = DocxTemplate(template_path)
    doc.render(context)
    doc.save(output_path)