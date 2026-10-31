import requests, json, io, time
from PIL import Image
import torch
import numpy as np
from transformers import CLIPModel, CLIPProcessor

vectors = []
succesful_art = []

model_id = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)

headers = {
    "User-Agent": "ArtSearch class project (gustavo.d29@k12.xrds.org)",
    "AIC-User-Agent": "ArtSearch class project (gustavo.d29@k12.xrds.org)",
}

with open("metadata.json", "r") as file:
    metadata = json.load(file)

for art in metadata:
    try:
        response = requests.get(
            "https://www.artic.edu/iiif/2/" + art["image_id"] + "/full/224,/0/default.jpg", 
            headers=headers
            )
        if response.ok:
            image_stream = io.BytesIO(response.content)
            image = Image.open(image_stream).convert("RGB")
            inputs = processor(images=image, return_tensors="pt")
            with torch.no_grad():
                features = model.get_image_features(**inputs)
            features = features/features.norm(dim=-1, keepdim=True)
            features = features.numpy()
            vectors.append(features[0])
            succesful_art.append(art)
        else:
            print(response.text[:500])
    except Exception as error:
        print(error)
        print(art["id"])
    time.sleep(0.5)
result = np.stack(vectors, axis=0)
np.save("embeddings.npy", result)
with open("embedded_metadata.json", "w", encoding="utf-8",) as file:
    json.dump(succesful_art, file)