import faiss
import numpy as np

# Load FAISS index
index = faiss.read_index("data/faiss.index")

# Load embeddings
embeddings_matrix = np.load("data/embeddings.npy")

# Pick an image embedding to search for (e.g., first image)
query_vector = embeddings_matrix[0].reshape(1, -1)  # Reshape for FAISS

# Perform search (returns top 5 similar images)
D, I = index.search(query_vector, 5)

print("Top 5 closest images (indices):", I)
print("Distances:", D)
