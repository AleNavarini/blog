'use strict'

function hover(element) {
    element.setAttribute('src', "static/images/logoFin.png");
  }
  
function unhover(element) {
    element.setAttribute('src', "static/images/logoIni.png");
  }

function checkForm() {
  $(document).ready(function() {
    console.log("entro");
    let pass = $("#password").val();
    let secondPass = $("#repeat_password").val();
    matchpass(pass, secondPass);
    return false;
  })
}

  function matchpass(firstPass, secondPass){    
      
    if(firstPass==secondPass) return true;  
    else alert("La contraseña debe ser la misma");  
    return false;  
    
  }