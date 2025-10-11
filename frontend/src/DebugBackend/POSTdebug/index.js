import Fetch from '../../FetchingAPIs/Fetch.js'; 
const fetching_data = new Fetch('/post'); 
const resp = await fetching_data.postData({"username": "Rijan", 
    "email": "rijangautam07@gmail.com", 
}); 
console.log(resp); 