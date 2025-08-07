import streamlit as st
import plotly.graph_objects as go

categories = [
    "Intensité concurrentielle",
    "Pouvoir de négociation des clients",
    "Pouvoir de négociation des fournisseurs",
    "Produits de substitution",
    "Menace de nouveaux entrants",
    "Pouvoir public"
]

values = [5, 4, 3, 2, 2, 3]
values += [values[0]]
categories += [categories[0]]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself',
    line_color='red',
    name="Forces de Porter"
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 5]
        )
    ),
    showlegend=False,
    title="Étoile sectorielle des cinq (+1) forces de Porter"
)

# 🔥 This line is critical!
st.plotly_chart(fig)