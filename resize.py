from PIL import Image
import json
import os

input_folder = "cover"
output_folder = "tiny"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open('./maidata.json', 'r', encoding='utf-8') as file:
    maidata = json.load(file)
    for item in maidata:
        input_path = os.path.join(input_folder, item["image_file"])
        output_path = os.path.join(output_folder, f"{item["id"]}.jpg")

        try:
            with Image.open(input_path) as img:
                img = img.resize((95, 95), Image.Resampling.LANCZOS)

                img.convert("RGB").save(output_path, "JPEG", quality=100)
        except OSError as e:
            print(f"Error processing {input_path}: {e}")
        except Exception as e:
            print(f"Unexpected error processing {input_path}: {e}")

print("Finish.")
