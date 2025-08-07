import plotly.graph_objects as go

# Données des 6 forces + retour au point initial pour fermer la forme
categories = [
    "Intensité concurrentielle", 
    "Pouvoir de négociation des clients", 
    "Pouvoir de négociation des fournisseurs", 
    "Produits de substitution", 
    "Menace de nouveaux entrants", 
    "Pouvoir public"
]

values = [5, 4, 3, 2, 2, 3]
values += [values[0]]  # pour fermer le polygone
categories += [categories[0]]

# Création du radar chart
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
            range=[0, 5],
            tickfont=dict(size=12)
        ),
        angularaxis=dict(
            tickfont=dict(size=13)
        )
    ),
    showlegend=False,
    title=dict(
        text="Étoile sectorielle des cinq (+1) forces de Porter",
        font=dict(size=18)
    )
)

fig.show()