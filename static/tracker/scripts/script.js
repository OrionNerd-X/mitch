document.getElementById("toggleSignup").addEventListener("click", function() {
    document.getElementById("loginBox").style.display = "none";
    document.getElementById("signupBox").style.display = "block";
    document.getElementById("toggleLogin").classList.remove("active");
    document.getElementById("toggleSignup").classList.add("active");
});

document.getElementById("toggleLogin").addEventListener("click", function() {
    document.getElementById("signupBox").style.display = "none";
    document.getElementById("loginBox").style.display = "block";
    document.getElementById("toggleSignup").classList.remove("active");
    document.getElementById("toggleLogin").classList.add("active");
});