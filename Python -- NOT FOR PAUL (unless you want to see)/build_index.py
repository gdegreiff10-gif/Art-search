import requests, json
from PIL import Image
import time

headers = {
    "User-Agent": "ArtSearch class project (example@gmail.com)",
    "AIC-User-Agent": "ArtSearch class project (example@gmail.com))",
}


holder = []
page_counter = 1
while True:
    response = requests.get(
    'https://api.artic.edu/api/v1/artworks?&limit=100&fields=id,title,artist_title,artwork_type_title,image_id&page=' + str(page_counter),
    headers=headers
    )
    
    print(response.status_code)
    if response.ok:
        wrapper = response.json()
        wrapper_2 = wrapper["pagination"]
        for art in wrapper["data"]:
            if art["artwork_type_title"] == "Painting" and art["image_id"] != None:
                holder.append(art)
    else:
        print(response.text[:500])
        break
    if wrapper_2["current_page"] >= wrapper_2["total_pages"]:
        break
    page_counter += 1
    time.sleep(1)
with open("metadata.json", "w", encoding="utf-8",) as file:
    json.dump(holder, file)
    