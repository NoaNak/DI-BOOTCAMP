setTimeout(createBanner, 2000);

function createBanner () {
    const section = document.querySelector("#container");
    const banner = document.createElement("p");
    const text = document.createTextNode("The sales end in 5sec");
    banner.appendChild(text);
    section.appendChild(banner);
}
