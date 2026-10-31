

async function getArt() {
    try {
        // 1. Get the search term from the search box, 
        //          send a request to the ombd (USING YOUR API KEY)
        //          decode the response as JSON
        search = document.getElementById("search").value
        let url = "https://api.artic.edu/api/v1/artworks/search?q=" + search + "&fields=id,title,artist_title,image_id"
        const headers = new Headers()
        headers.append("Accept", "application/json")
        const response = await fetch(url, {headers:headers})
        const json = await response.json()
        console.log(json)

        const artHolder = document.getElementById("artHolder");
        artHolder.textContent = ""
        const config = json.config
        for (const artwork of json.data) {
            if (!artwork.image_id) continue;
            const divContainer = document.createElement("div")
            divContainer.classList.add("card")  

            const image = document.createElement("img")
            image.src = config.iiif_url + "/" + artwork.image_id + "/full/843,/0/default.jpg";
            // image.width = "300"



            const card = document.createElement("div")
            card.classList.add("container")
            const titleHeader = document.createElement("h3")
            titleHeader.textContent = artwork.title

            card.appendChild(titleHeader)

            divContainer.appendChild(image);
            divContainer.appendChild(card)

            artHolder.appendChild(divContainer)
        }


    }
    catch (error) {
        console.log(error)
    }
}