import Fetch from "./src/utils/fetch.js";
import LoadTemplate from "./src/utils/loadtemplate.js";
import Handle_Login from "./src/pages/auth/login/script.js";
import GetCookie from "./src/utils/getcookie.js";
import Handle_Home from "./src/pages/home/script.js"; 

const root = document.querySelector("#root");

const main = async () => {
  try {
    const sessionid = GetCookie("sessionid");
    if (sessionid) {
      const fetching_data = new Fetch("/validate-session");
      const resp = await fetching_data.postData({
        cookies: {
          sessionid: sessionid,
        },
      });
      console.log(resp); // debug

      if(!resp){
        console.error("No response from the server"); 
        root.innerHTML = "<h1>No response from Rijan's server</h1>";  
        return; 
      };

      if(resp.status == "Failed"){
        root.innerHTML = await LoadTemplate('./src/pages/auth/login'); 
        Handle_Login(); 
        console.error(resp); 
      };

      if(resp.status == "Success"){
        root.innerHTML = await LoadTemplate('./src/pages/home'); 
        Handle_Home(resp.user_data.username, resp.user_data.email); 
        console.log("Session Validated!", resp);
      }; 

    }
    else{
      root.innerHTML = await LoadTemplate('./src/pages/auth/login'); 
      Handle_Login(); 
      console.warn(`Authentication needed. Sessionid = ${sessionid}`)
    }
  } catch (err) {
    console.error("Error occured", err);
  }
};

main(); 
