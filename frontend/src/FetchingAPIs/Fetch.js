export default class Fetch{
    constructor(url){
        this.url = url
        this.BASE_URL = 'http://localhost:8000'
        try {
    }
    async getData(){
            const response = await fetch(`${this.BASE_URL}${this.url}`, {
                method : "Get",
                headers: {
                    "content-type" : "application/json"
                } , 

            }); 
            if(!response.ok){
                throw new Error("HTTP server Error", response.status)
            }

            const data = (await response).json(); 
            return data
         }
        catch(error){
            console.error("Error fetching data :(", error)
        }
        
    }
    async postData(body = {}) {
    try {
        const response = await fetch(`${this.BASE_URL}${this.url}`, {
            method: "POST", 
            headers: {
                "Content-Type": "application/json" 
            },
            body: JSON.stringify(body),
        });

        if (!response.ok) {
            throw new Error(`HTTP server error: ${response.status}`);
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error("Error posting data :(", error);
    }
}

}; 