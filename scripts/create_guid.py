import os
import uuid

base_path = "datasets"

subfolders = ["test", "train", "val"]

image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

for subfolder in subfolders:
    folder_path = os.path.join(base_path, subfolder)
    if not os.path.exists(folder_path):
        print(f"Pasta {folder_path} não encontrada!")
        continue

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(image_extensions):
            new_name = f"{uuid.uuid4()}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(file_path, new_path)
            print(f"Renomeado: {file_path} -> {new_path}")

print("Renomeação concluída!")