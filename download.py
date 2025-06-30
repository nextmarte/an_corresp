import os
import kagglehub
import shutil

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "dados")

# Create data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Download latest version (kagglehub doesn't support target_dir directly)
path = kagglehub.dataset_download("adaoduque/campeonato-brasileiro-de-futebol")

print("Path to dataset files:", path)

# Copy all files to the data directory
try:
    for root, dirs, files in os.walk(path):
        for file in files:
            src = os.path.join(root, file)
            dst = os.path.join(data_dir, file)
            shutil.copy2(src, dst)
    print(f"Arquivos copiados com sucesso para: {data_dir}")
except Exception as e:
    print(f"Erro ao copiar arquivos: {e}")