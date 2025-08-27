import argparse
from PIL import Image

def downscale_image(input_path: str, output_path: str, target_resolution: int):
    try:
        img = Image.open(input_path)
        # Downscale using nearest-neighbor for pixel art effect
        img_small = img.resize((target_resolution, target_resolution), Image.NEAREST)
        img_small.save(output_path)
        print(f"Image downscaled and saved to {output_path}")
    except Exception as e:
        print(f"Error downscaling image: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downscale an image to a target resolution.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input image.")
    parser.add_argument("--output", type=str, required=True, help="Path to save the downscaled image.")
    parser.add_argument("--res", type=int, default=64, help="Target resolution (e.g., 32, 64).")
    
    args = parser.parse_args()
    downscale_image(args.input, args.output, args.res)