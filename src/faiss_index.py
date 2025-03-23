import faiss
import numpy as np

# Load embeddings from file
embeddings_matrix = np.load("src/data/embeddings.npy")

# Initialize FAISS index (L2 distance for similarity search)
d = embeddings_matrix.shape[1]  # Dimensionality of embeddings
index = faiss.IndexFlatL2(d)  # L2 distance-based index
index.add(embeddings_matrix)  # Add embeddings to the index

# Save FAISS index
faiss.write_index(index, "src/data/faiss.index")
print("Saved FAISS index to src/data/faiss.index")
