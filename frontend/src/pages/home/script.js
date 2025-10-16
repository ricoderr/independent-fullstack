const Handle_Home = (name, email)=>{
    const name_place = document.querySelector('.name');
    const email_place = document.querySelector('.email');
    name_place.innerHTML = name; 
    email_place.innerHTML = `Email: ${email}`
}

export default Handle_Home; 