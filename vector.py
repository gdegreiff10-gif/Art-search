import requests, json, io, time
from PIL import Image
import torch
import numpy as np
from transformers import CLIPModel, CLIPProcessor

vectors = []
succesful_art = []

headers = {
    "User-Agent": "ArtSearch class project (gustavo.d29@k12.xrds.org)",
    "AIC-User-Agent": "ArtSearch class project (gustavo.d29@k12.xrds.org)",
}

with open("metadata.json", "r") as file:
    metadata = json.load(file)

for art in metadata:
    response = requests.get(
        "https://www.artic.edu/iiif/2/" + art["image_id"] + "/full/224,/0/default.jpg", 
        headers=headers
        )