import requests, json, io, time
from PIL import Image
import torch
import numpy as np
from transformers import CLIPModel, CLIPProcessor

model_id = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)

images_vectors = np.load('./data/embeddings.npy')
metadata = json.load('./data/embedded_metadata.json')

query = 'a lonely city at night'

inputs = processor(text=query, return_tensors="pt", padding=True)

with torch.no_grad():
    text_out = model.text_model(**inputs)
    query_vector = model.text_projection(text_out.pooler_output)
