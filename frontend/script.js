import Fetch from "./src/utils/fetch.js";
import LoadTemplate from "./src/utils/loadtemplate.js"

const root = document.querySelector('#root'); 

const fetching_cookies = new Fetch('/validate-session'); 
const resp = fetching_cookies().postData(credentials = "include"); 

// resp will have the object of the response sent by the server.

// if the sessionid in the cookies sent by the frontend is present in the db
// then, server will respond with the data of the user who owns the sessionid. 

// else if the sessionid in the cookies sent by the frontend is null 
// then, the server will response with status: "Failed" by which the frontend will show the login page in "/" url.

if(resp["status"] === "Failed"){
    root.innerHTML = LoadTemplate('/pages/auth/login'); 
}
else{
    
}