// setTimeout(createBanner, 10000);
// Faire un decompte 

let idInterval;

function createBanner () {
    const section = document.querySelector("#container");
    const banner = document.createElement("p");
    banner.setAttribute("id", "banner");
    section.appendChild(banner);
    idInterval = setInterval(changeNumber, 1000);
}

createBanner();

let counter = 10;

function changeNumber(){
    if(counter === 0) {
        clearInterval(idInterval);
    } 
        const bannerParagraph = document.querySelector("#banner");
        bannerParagraph.textContent =  `The sales end in ${counter} sec`;
        counter --;

    }



