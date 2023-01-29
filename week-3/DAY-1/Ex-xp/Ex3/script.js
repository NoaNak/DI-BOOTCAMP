// In the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
const nav = document.getElementById("navBar");
nav.setAttribute("id", "socialNetworkNavigation");

// We are going to add a new <li> to the <ul>.
// 1- First, create a new <li> tag (use the createElement method).
const newLi = document.createElement("li");
const node = document.createTextNode("Logout");
newLi.appendChild(node);
document.getElementsByTagName("ul")[0].appendChild(newLi);
