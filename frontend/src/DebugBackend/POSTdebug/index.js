import Fetch from '../../FetchingAPIs/Fetch.js'; 

const form = document.querySelector('.form'); 
const username_input = document.querySelector('#username');
const email_input = document.querySelector('#email');
const resp_box = document.querySelector('.resp_box'); 

form.addEventListener("submit", async (event) =>{
    event.preventDefault(); 

    const username = username_input.value.trim(); 
    const email = email_input.value.trim(); 

    if(!username || !email){
        alert("Please enter the values in username and email"); 
        console.warn("Please enter the values in username and email"); 
        return; 
    }
    const fetching_data = new Fetch('/post'); 
    const resp = await fetching_data.postData({"username": username, 
        "email": email, 
    }); 
    resp_box.innerHTML = `method: ${resp.method}, status: ${resp.status} `  ; 
    

})


