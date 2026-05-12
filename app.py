from pathlib import Path

import streamlit as st

from src.context_builder import build_context
from src.docx_renderer import render_ordre_mission
from src.forms import mission_inputs, missionnaire_inputs, signature_inputs
from src.forms import trajet_inputs


ROOT_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = ROOT_DIR / "templates" / "ordre_mission_template.docx"
GENERATED_DIR = ROOT_DIR / "generated"

st.set_page_config(page_title="OM Editor", page_icon="📄")

st.title("📄 OM Editor")

with st.form("om_form"):
    missionnaire = missionnaire_inputs()
    mission = mission_inputs()

    st.header("3. Trajet aller")
    aller_1 = trajet_inputs("aller_1", "Aller 1", "Bruz", "Rennes")
    aller_2 = trajet_inputs("aller_2", "Aller 2", "Rennes", "")

    st.header("4. Trajet retour")
    retour_1 = trajet_inputs("retour_1", "Retour 1", "", "Rennes")
    retour_2 = trajet_inputs("retour_2", "Retour 2", "Rennes", "Bruz")

    st.header("5. Convenances personnelles")
    perso_1 = trajet_inputs("perso_1", "Période personnelle 1")
    perso_2 = trajet_inputs("perso_2", "Période personnelle 2")

    signature = signature_inputs(missionnaire["ville"])

    submitted = st.form_submit_button("Générer l'ordre de mission")

if submitted:
    context = build_context(
        missionnaire=missionnaire,
        mission=mission,
        signature=signature,
        trajets=[
            aller_1,
            aller_2,
            retour_1,
            retour_2,
            perso_1,
            perso_2,
        ],
    )

    GENERATED_DIR.mkdir(exist_ok=True)

    output_path = (
        GENERATED_DIR
        / f"OM_{context['nom']}_{context['prenom']}.docx"
    )

    render_ordre_mission(
        template_path=TEMPLATE_PATH,
        output_path=output_path,
        context=context,
    )

    st.success("Ordre de mission généré.")

    with open(output_path, "rb") as file:
        st.download_button(
            label="Télécharger le document",
            data=file,
            file_name=output_path.name,
            mime=(
                "application/vnd.openxmlformats-"
                "officedocument.wordprocessingml.document"
            ),
        )