import os

def remove_duplicates(label_dir):
    for file in os.listdir(label_dir):
        if file.endswith(".txt"):
            path = os.path.join(label_dir, file)
            with open(path, "r") as f:
                lines = f.readlines()
            unique_lines = list(set(lines))
            with open(path, "w") as f:
                f.writelines(unique_lines)
            
label_directory = "datasets/test/labels", 
remove_duplicates(label_directory)
print("Duplicate labels removed.")
