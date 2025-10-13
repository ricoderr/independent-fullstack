import Fetch from "../../FetchingAPIs/Fetch.js"

const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const email = formData.get("email").trim();
  const password = formData.get("password").trim();

  if (!email || !password) {
    alert("Please fill in all fields");
    return;
  }

  const loginData = {
    email,
    password
  };

  const fetching_data = new Fetch('/auth/login'); 
  const resp = await fetching_data.postData(loginData); 

  console.log("Login Data:", loginData);

  console.log(resp); 

  const sessionid = resp["user_data"]["sessionid"]
  document.cookie = `sessionid=${sessionid};  expires=Fri, 31 Dec 2025 23:59:59 GMT; path=/`

  



  alert("Login successful!");
  form.reset();
});
