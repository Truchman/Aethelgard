
import argparse
import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part

def generate_png_asset(project_id: str, location: str, prompt: str, output_file: str, reference_image_paths: list[str] = None):
    """Génère une image PNG en utilisant un modèle multimodal de Vertex AI."""
    
    print(f"Initialisation de Vertex AI pour le projet '{project_id}' dans '{location}'...")
    vertexai.init(project=project_id, location=location)
    
    # Utiliser un modèle qui supporte les entrées multimodales
    model = GenerativeModel("imagegeneration@006")

    prompt_parts = []
    if reference_image_paths:
        for path in reference_image_paths:
            if not os.path.exists(path):
                print(f"Erreur : Image de référence non trouvée à '{path}'")
                continue
            print(f"Utilisation de l'image de référence : {path}")
            # Charger l'image comme un objet Part
            with open(path, "rb") as f:
                image_data = f.read()
            prompt_parts.append(Part.from_data(image_data, mime_type="image/png"))

    # Ajouter le prompt textuel à la fin
    prompt_parts.append(prompt)

    print(f"Génération de l'image pour le prompt : '{prompt}'...")
    
    try:
        # Générer le contenu en utilisant le prompt multimodal
        response = model.generate_content(prompt_parts)
        
        # S'assurer que la réponse contient une image
        if response.parts and response.parts[0].mime_type.startswith("image/"):
            image_data = response.parts[0]._raw_part.blob.data
            with open(output_file, "wb") as f:
                f.write(image_data)
            print(f"Image générée et sauvegardée avec succès dans '{output_file}'")
        else:
            print("Aucune image n'a été générée. Réponse du modèle :")
            print(response)

    except Exception as e:
        print(f"Une erreur est survenue lors de la génération de l'image : {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générer des assets PNG avec Vertex AI (modèle multimodal).")
    parser.add_argument("--project", type=str, required=True, help="Votre ID de projet Google Cloud.")
    parser.add_argument("--location", type=str, default="us-central1", help="La localisation Google Cloud (ex: 'us-central1').")
    parser.add_argument("--prompt", type=str, required=True, help="Le prompt décrivant l'image à générer.")
    parser.add_argument("--ref", type=str, nargs='*', help="Optionnel : Chemin vers une ou plusieurs images de référence pour le style.")
    parser.add_argument("--out", type=str, default="generated_image.png", help="Nom du fichier de sortie pour le PNG.")
    
    args = parser.parse_args()

    generate_png_asset(
        project_id=args.project,
        location=args.location,
        prompt=args.prompt,
        reference_image_paths=args.ref,
        output_file=args.out
    )
