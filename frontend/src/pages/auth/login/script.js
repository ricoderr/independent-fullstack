import Fetch from "../../../utils/fetch.js";

const Handle_Login = () => {
  const form = document.querySelector("form");
  if (!form) return; // safety check

  // Prevent attaching multiple listeners
  if (form.dataset.listenerAttached) return;
  form.dataset.listenerAttached = "true";

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const email = formData.get("email").trim();
    const password = formData.get("password").trim();

    if (!email || !password) {
      alert("Please fill in all fields");
      return;
    }

    const loginData = { email, password };

    try {
      const fetching_data = new Fetch("/auth/login");
      const resp = await fetching_data.postData(loginData);

      console.log("Login Data:", loginData);
      console.log(resp);

      if (resp.status === "Success" && resp.user_data?.sessionid) {
        document.cookie = `sessionid=${resp.user_data.sessionid}; expires=Fri, 31 Dec 2025 23:59:59 GMT; path=/; SameSite=Strict`;
        alert(resp.message || "Login successful");
        window.location.replace("/"); // reload to home
      } else {
        alert(resp.message || "Login failed");
      }
    } catch (err) {
      console.error("Login error:", err);
      alert("An error occurred during login.");
    }

    form.reset();
  });
};

export default Handle_Login;
