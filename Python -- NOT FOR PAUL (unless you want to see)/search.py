import requests, json, io, time
from PIL import Image
import torch
import numpy as np
from transformers import CLIPModel, CLIPProcessor


model_id = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)



images_vectors = np.load('./data/embeddings.npy')
with open("./data/embedded_metadata.json", "r") as file:
    metadata = json.load(file)

input = " "
query = 'a painting of ' + input

inputs = processor(text=query, return_tensors="pt", padding=True)

with torch.no_grad():
    text_out = model.text_model(**inputs)
    query_vector = model.text_projection(text_out.pooler_output)
query_vector = query_vector/query_vector.norm(dim=-1, keepdim=True)
query_vector = query_vector.numpy()

query_vector = query_vector[0]

dot_product = images_vectors @ query_vector

best_match = np.argsort(dot_product)[::-1]
best_match = best_match[:5]

for i in best_match:
    print(metadata[i]["title"])
    print(metadata[i]["artist_title"])
    print(dot_product[i])
    