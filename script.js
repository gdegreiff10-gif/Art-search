

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

        const movieHolder = document.getElementById("movieHolder");
        movieHolder.textContent = ""
        const config = json.config
        for (const artwork  of json.data) {
            //  Create a div to hold each image and title 
            //  Give the div the css class of CARD
            const wrapper = document.createElement("div")
            wrapper.classList.add("card")

            // Create an image element
            //      point it to the image from this movie            
            const image = document.createElement("img")
            
            image.src = config.iiif_url + "/" + artwork.image_id + "/full/843,/0/default.jpg";
            image.width = "500"


            // Create a CONTAINER div to hold the title and year.
            // Give the CONTAINER div the style of container
            const container = document.createElement("div")
            container.textContent = json.title
            container.classList.add("container")
            // Add the CONTAINER to the CARD
            wrapper.append(container)

            // Add all the elements to the movieHolder element
            movieHolder.append(image)
            movieHolder.append(wrapper)
        }


    }
    catch (error) {
        console.log(error)
    }
}