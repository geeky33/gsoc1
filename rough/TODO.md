1. To access CLIP Models
2. to create text embeddings(convert text to vectors)
3. to create image embeddings(convert imgs to vec)
4. to store these vec emb in FAISS format
5. to analyse the similarity score
6. compute the pca (froom 1x800 dim) to 1x3 by retaining only 3 pc. there will be a loss of info but we have to also compute along how much info loss is occuring.
7. now we are gonna make the 3d plot for 1x3 
8. contigency issues:we might have to increase it later from 3.
so we will just plot 2d.