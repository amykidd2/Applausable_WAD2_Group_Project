function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.innerHTML === "Your email:") {
        x.innerHTML = "Your email:" + email;
    } else {
        x.innerHTML = "Your email:";
    }
}