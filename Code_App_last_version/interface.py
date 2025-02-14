import app
import gradio as gr
import paths


# Chargement des données
df = app.load_df(paths.salles_path)
df_photo = app.load_df(paths.photographes_path)
df_traiteur = app.load_df(paths.traiteurs_path)
df_fleuriste = app.load_df(paths.fleuristes_path)

def get_htmls(address):

    #salles
    salles_df = app.get_best_address(address, df)
    print(f"result \n : {salles_df}")
    map_salles = app.add_markers_from_dataframe(salles_df, address)

    # photographes
    ptg_df = app.get_best_address(address, df_photo)
    print(f"result \n : {ptg_df}")
    map_ptg = app.add_markers_from_dataframe(ptg_df, address)

    # traiteurs
    traiteur_df = app.get_best_address(address, df_traiteur)
    print(f"result \n : {traiteur_df}")
    map_traiteur = app.add_markers_from_dataframe(traiteur_df, address)


    # fleuriste
    fl_df = app.get_best_address(address, df_fleuriste)
    print(f"result \n : {fl_df}")
    map_fl = app.add_markers_from_dataframe(fl_df, address, rat=False)
    return map_salles._repr_html_(), map_ptg._repr_html_() , map_traiteur._repr_html_() , map_fl._repr_html_()



with gr.Blocks() as demo:
    gr.Markdown("## Localisation des lieux de réception et des prestataires")
    text_area = gr.Textbox(placeholder="Entrez une adresse", show_label=False)
    search_btn = gr.Button("Afficher la carte")
    with gr.Tab("Lieux de réception"):
        carte_area = gr.HTML()
    with gr.Tab("Photographes"):
        ptg_area = gr.HTML()
    with gr.Tab("Traiteurs"):
        traiteur_area = gr.HTML()
    with gr.Tab("Fleuristes"):
        fl_area = gr.HTML()

    search_btn.click(
        fn=get_htmls,
        inputs=text_area,
        outputs=[carte_area, ptg_area, traiteur_area, fl_area]
    )

demo.launch()