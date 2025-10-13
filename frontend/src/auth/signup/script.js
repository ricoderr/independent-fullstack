import Fetch from '../../FetchingAPIs/Fetch.js'; 

const form = document.querySelector("form");


form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const username = formData.get("username").trim();
  const email = formData.get("email").trim();
  const password = formData.get("password").trim();
  const confirmPassword = formData.get("Cpassword").trim();

  if (!username || !email || !password || !confirmPassword) {
    alert("Please fill in all fields");
    return;
  }

  if (password !== confirmPassword) {
    alert("Passwords do not match!");
    return;
  }

  const userData = {
    username,
    email,
    password
  };

  console.log("User Data:", userData);
  const fetching_data = new Fetch('/auth/signup'); 
  const resp = await fetching_data.postData(userData); 
  console.log(resp) 
  alert("Signup successful!");
  form.reset();
});
