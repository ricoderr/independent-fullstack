import Fetch from "./src/utils/fetch.js";
import LoadTemplate from "./src/utils/loadtemplate.js";
import Handle_Login from "./src/pages/auth/login/script.js";

const root = document.querySelector("#root");

const main = async () => {
  try {
    const fetching_cookies = new Fetch("/validate-session");
    const resp = await fetching_cookies.postData();

    console.log("Session response:", resp);

    if (!resp) {
      root.innerHTML = "<h1>Error: No response from server</h1>";
      return; 
    }

    if (resp.status === "Failed") {
      root.innerHTML = await LoadTemplate("./src/pages/auth/login/index.html");

      Handle_Login();
    } else {
      root.innerHTML = await LoadTemplate("./src/pages/home.html");
    }
  } catch (err) {
    console.error("Error in main:", err);
    root.innerHTML = "<h1>Unexpected Error</h1>";
  }
};

document.addEventListener("DOMContentLoaded", main);
