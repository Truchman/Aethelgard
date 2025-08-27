
import argparse
import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

# --- CONFIGURATION & SÉCURITÉ ---
# Ce script utilise les "Application Default Credentials" (ADC).
# Assurez-vous d'avoir exécuté `gcloud auth application-default login`.

def generate_png_asset(project_id: str, location: str, prompt: str, output_file: str, reference_image_path: str = None):
    """Génère une image PNG en utilisant le modèle Imagen de Vertex AI."""
    
    print(f"Initialisation de Vertex AI pour le projet '{project_id}' dans '{location}'...")
    vertexai.init(project=project_id, location=location)
    
    model = ImageGenerationModel.from_pretrained("imagegeneration@006")

    # L'influence du style de l'image de référence se fait principalement via le prompt.
    # Les API d'édition d'image plus complexes permettent un contrôle plus fin.
    final_prompt = prompt
    if reference_image_path:
        if not os.path.exists(reference_image_path):
            print(f"Erreur : Image de référence non trouvée à '{reference_image_path}'")
            return
        print(f"Utilisation de l'image de référence : {reference_image_path}")
        final_prompt = f"{prompt}, dans un style similaire à l'image de référence fournie."

    print(f"Génération de l'image pour le prompt : '{final_prompt}'...")
    
    try:
        response = model.generate_images(
            prompt=final_prompt,
            number_of_images=1,
            # D'autres paramètres peuvent être ajoutés ici (ex: seed, aspect_ratio)
        )
        
        image = response[0]
        image.save(location=output_file, include_generation_parameters=False)
        
        print(f"Image générée et sauvegardée avec succès dans '{output_file}'")

    except Exception as e:
        print(f"Une erreur est survenue lors de la génération de l'image : {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générer des assets PNG avec Vertex AI Imagen.")
    parser.add_argument("--project", type=str, required=True, help="Votre ID de projet Google Cloud.")
    parser.add_argument("--location", type=str, default="us-central1", help="La localisation Google Cloud (ex: 'us-central1').")
    parser.add_argument("--prompt", type=str, required=True, help="Le prompt décrivant l'image à générer.")
    parser.add_argument("--ref", type=str, help="Optionnel : Chemin vers une image de référence pour le style.")
    parser.add_argument("--out", type=str, default="generated_image.png", help="Nom du fichier de sortie pour le PNG.")
    
    args = parser.parse_args()

    generate_png_asset(
        project_id=args.project,
        location=args.location,
        prompt=args.prompt,
        reference_image_path=args.ref,
        output_file=args.out
    )
