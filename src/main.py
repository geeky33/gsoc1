import os
import torch
import clip
import numpy as np
from PIL import Image
from embeddings.compute import get_image_embedding

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Folder where images are stored
image_folder = "src/data/images/"
image_files = os.listdir(image_folder)

embeddings = []
for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    image = Image.open(img_path)
    embedding = get_image_embedding(model, image, device)
    embeddings.append(embedding.flatten())  # Convert to 1D vector

# Convert embeddings list to NumPy array
embeddings_matrix = np.array(embeddings)  # Shape: (num_images, embedding_dim)

# Save embeddings to a file
np.save("src/data/embeddings.npy", embeddings_matrix)
print(f"Saved embeddings to src/data/embeddings.npy with shape {embeddings_matrix.shape}")
