import gradio as gr

# Define possible genres
genres = unique_generes.tolist()
iface = gr.Interface(
    fn=search,
    inputs=[
        gr.Textbox(lines=5, placeholder="Escribe aquÃ­ tu consulta...", label="Consulta"),
        gr.Dropdown(choices=genres, label="GÃ©nero de la pelÃ­cula"),
        gr.Slider(minimum=1, maximum=10, value=5, label="PuntuaciÃ³n mÃ­nima"),
        gr.Number(minimum=1, maximum=10, value=3, label="NÃºmero de resultados")

    ],
    outputs=gr.Dataframe(type="pandas", label="Resultados"),
    title="Buscador de pelÃ­culas",
    description="Introduce tu consulta, selecciona un gÃ©nero y define una puntuaciÃ³n mÃ­nima para buscar pelÃ­culas.",
)

# Launch the interface
iface.launch()