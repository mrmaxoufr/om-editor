from pathlib import Path

from docxtpl import DocxTemplate


def render_ordre_mission(
    template_path: Path,
    output_path: Path,
    context: dict,
) -> None:
    doc = DocxTemplate(template_path)
    doc.render(context)
    doc.save(output_path)