var loginModal = document.getElementById("loginModal");
var registerModal = document.getElementById("registerModal");

var loginBtn = document.querySelector(".btnLogin-popup");
var closeLogin = document.getElementById("closeLogin");
var closeRegister = document.getElementById("closeRegister");
var signUpLink = document.querySelector("#loginModal a[href='registration.html']");

loginBtn.onclick = function() {
    loginModal.style.display = "block";
}
signUpLink.onclick = function(event) {
    event.preventDefault();
    registerModal.style.display = "block";
    loginModal.style.display = "none";
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