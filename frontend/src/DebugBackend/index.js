import Fetch from '../FetchingAPIs/Fetch.js'; 
const Response_Name = document.querySelector(".response_name");
const Response_Message = document.querySelector(".response_message");
const Response_Status = document.querySelector(".response_status");

const form = document.querySelector('.form');
const input = document.getElementById('url');

form.addEventListener('submit', async (event) => {
  event.preventDefault(); 

  const urlPath = input.value.trim();

  if (!urlPath) {
    alert("Please enter a URL path!"); 
    console.warn("Please enter a URL path!");
    return;
  }
  const data_fetcher = new Fetch(urlPath); 
  const data = await data_fetcher.getData(); 
  console.log(data); 
  
  Response_Name.innerHTML = data.name;
  Response_Message.innerHTML = data.message;
  Response_Status.innerHTML = data.status;
  if (data.status == "success"){
      Response_Status.style.color = "Green";
  }
  else{
      Response_Status.style.color = "Red"; 
  }
  
});
