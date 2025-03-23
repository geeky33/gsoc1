import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os
from embeddings.compute import get_image_embedding
import clip
import torch
from PIL import Image

# Load model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Load multiple images and compute embeddings
image_folder = "data/images/"  # Folder containing images
image_files = os.listdir(image_folder)

embeddings = []
for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    image = Image.open(img_path)
    embedding = get_image_embedding(model, image, device)
    embeddings.append(embedding.flatten())  # Flatten to 1D vector

# Convert list to NumPy array
embeddings_matrix = np.array(embeddings)  # Shape: (100, 800)

# Apply PCA
pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(embeddings_matrix)  # Shape: (100, 3)

# Visualize in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], reduced_embeddings[:, 2])
ax.set_title("3D Visualization of Image Embeddings")
plt.show()
