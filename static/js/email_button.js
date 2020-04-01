function myFunction() {
    var emailElement = document.getElementById("myDIV");
    if (emailElement.innerHTML === "Your email:") {
        emailElement.innerHTML = "Your email:" + email;
    } else {
        emailElement.innerHTML = "Your email:";
    }
}