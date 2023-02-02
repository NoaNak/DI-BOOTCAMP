let chesseCake = "https://cdn.shopify.com/s/files/1/0613/7842/9113/products/51dhISarTgL_1024x1024.jpg?v=1644049468";
    
let imagesDiv = document.getElementById("images");

function addListenerToImage(){
    const allImages = document.querySelectorAll("img");
    for(let img of allImages){
        img.addEventListener("click", showImages);
    }
}

function showImages(){

}