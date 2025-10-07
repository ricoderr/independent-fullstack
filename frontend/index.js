import Fetch from './src/FetchingAPIs/Fetch.js'; 
const fetching_data = new Fetch('/post'); 
const resp = await fetching_data.postData({"name": "Rijan"}); 
console.log(resp); 