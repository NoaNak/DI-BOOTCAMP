

   let language = prompt('which language do you speak ?');
   let lower = language.toLocaleLowerCase();

    if(lower == "french"){
        console.log("Bonjours");
    }
    
    else if(lower == "english"){
        console.log("Hello");
    }

    else if(lower == "hebrew"){
        console.log("Shalom");
    }
    
    else{
        console.log("01110011 01101111 01110010 01110010 01111001");
    }
