from pathlib import Path

from src.docx_renderer import render_ordre_mission
from src.sample_data import SAMPLE_CONTEXT


ROOT_DIR = Path(__file__).resolve().parents[1]

template_path = ROOT_DIR / "templates" / "ordre_mission_template.docx"
output_path = ROOT_DIR / "generated" / "ordre_mission_test.docx"

output_path.parent.mkdir(exist_ok=True)

render_ordre_mission(
    template_path=template_path,
    output_path=output_path,
    context=SAMPLE_CONTEXT,
)

print(f"Document généré : {output_path}")