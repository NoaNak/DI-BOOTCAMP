// Retrieve the form and console.log it.
const form = document.querySelector('form');
console.log(form);

// Retrieve the inputs by their id and console.log them.
// Retrieve the inputs by their name attribute and console.log them.
// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.

const fname = document.querySelector('fname')[0];
console.log(fname);

const lname = document.querySelector('lname')[0];
console.log(lname);

const button = document.querySelector('#submit');
button.addEventListener("click", submit());

function submit(event){
    event.preventDefault();
    //it stops the default action of the submission
    //the page will not refresh    
    const name = fname.value;
    const lastname = lname.value; 
    if (!name || !lastname){
        return;
    }
}


