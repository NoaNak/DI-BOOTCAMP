let button = document.getElementById('button');
let animate = document.getElementById('animate');

button.addEventListener("click", animatePassing);

function animatePassing() {
      let start = Date.now(); 

      let timer = setInterval(function() {
        let timePassed = Date.now() - start;
        console.log(timePassed)
        animate.style.left = timePassed / 5.9 + 'px';
        if (timePassed > 2000) {
          clearInterval(timer);
        }
      }, 20);
    }
console.log('hey');