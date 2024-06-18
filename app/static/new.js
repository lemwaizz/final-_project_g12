document.addEventListener('DOMContentLoaded', () => {
    let searchForm = document.querySelector('.search-form');
    document.querySelector('#search-btn').onclick = () => {
        searchForm.classList.toggle('active');
        loginModal.classList.remove('active');
        navbar.classList.remove('active');
        signUpLink.classList.remove('active');
    };
});

var loginModal = document.getElementById("loginModal");
var registerModal = document.getElementById("registerModal");

var loginBtn = document.querySelector("#login-btn");
var closeLogin = document.getElementById("closeLogin");
var closeRegister = document.getElementById("closeRegister");
var signUpLink = document.querySelector("#loginModal a[href='registration.html']");

loginBtn.onclick = function() {
    loginModal.style.display = "block";
    registerModal.style.display = "none";
    navbar.classList.remove('active');
    signUpLink.classList.remove('active');	
}
signUpLink.onclick = function(event) {
    event.preventDefault();
    registerModal.style.display = "block";
    loginModal.style.display = "none";
    navbar.classList.remove('active');
    signUpLink.classList.remove('active');
}
closeLogin.onclick = function() {
    loginModal.style.display = "none";
}
closeRegister.onclick = function() {
    registerModal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
    } else if (event.target == registerModal) {
        registerModal.style.display = "none";
    }
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    loginModal.classList.remove('active');
    signUpLink.classList.remove('active');
};

window.onscroll = () => {
    searchForm.classList.remove('active');
    loginModal.classList.remove('active');
    navbar.classList.remove('active');
    signUpLink.classList.remove('active');
};

