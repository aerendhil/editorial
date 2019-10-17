//Validación login
$("#form_login").validate({
    rules: {
        "txtCorreo":{
            required: true,
            email: true
        },
        "txtPassword":{
            required: true,
            minlength: 6
        }
    },
    messages:{
        "txtCorreo":{
            required: "Debe llenar el campo antes de continuar",
            email: "Formato de correo incorrecto"
        },
        "txtPassword":{
            required: "Debe llenar el campo antes de continuar",
            minlength: "La contraseña es demasiado corta"
        }
    }
});

$("#form_registro").validate({
    rules: {
        "txtCorreo":{
            required: true,
            email: true
        },
        "txtRun":{
            required: true,
            validarRut: true,
        },
        "txtNombres":{
            required: true,
            lettersonly: true
        },
        "txtApellidos":{
            required: true,
            lettersonly: true
        },
        "dtpNacimiento":{
            required: true,
            validarFecha: true
        },
        "txtTelefono":{
            required: true,
            numbersonly: true
        },
        "cmbRegion":{
            required: true
        },
        "cmbCiudad":{
            required: true
        },
        "cmbComuna":{
            required: true
        },
        "cmbVivienda":{
            required: true
        }
    },
    messages:{
        "txtCorreo":{
            required: "Ingrese su correo.",
            email: "El correo ingresado no cumple con el formato."
        },
        "txtRun":{
            required: "Ingrese su run",
            validarRut: "El formato del rut es incorrecto.",
        },
        "txtNombres":{
            required: "Ingrese sus nombres.",
            lettersonly: "Ingrese solo letras."
        },
        "txtApellidos":{
            required: "Ingrese sus apellidos.",
            lettersonly: "Ingrese solo letras."
        },
        "dtpNacimiento":{
            required: "Ingrese su fecha de nacimiento.",
            validarFecha: "La fecha de nacimiento debe ser anterior a 2001."
        },
        "txtTelefono": {
            required: "Ingrese su número de teléfono.",
            numbersonly: "Ingrese solo números."
        },
        "cmbRegion":{
            required: "Seleccione una región."
        },
        "cmbCiudad":{
            required: "Seleccione una ciudad."
        },
        "cmbComuna":{
            required: "Seleccione una comuna."
        },
        "cmbVivienda":{
            required: "Seleccione el tipo de vivienda."
        }
    }
});

jQuery.validator.addMethod("lettersonly", function(value, element) {
    return this.optional(element) || /^[a-z]+ ?[a-z]+$/i.test(value);
  });
  
jQuery.validator.addMethod("numbersonly", function(value, element) {
    return this.optional(element) || /^[0-9]+$/i.test(value);
}); 

jQuery.validator.addMethod("validarRut", function(value, element){
    return this.optional(element) || rut(value);
});

jQuery.validator.addMethod("validarFecha", function(value, element){
    return this.optional(element) || fecha(value);
});

function rut(rutCompleto){
	if ( rutCompleto.length == 0 ){ return false; }
	if ( rutCompleto.length < 8 ){ return false; }

	rutCompleto = rutCompleto.replace('-','')
	rutCompleto = rutCompleto.replace(/\./g,'')

    if (rutCompleto.length > 9) { return false; }

	var suma = 0;
	var caracteres = "1234567890kK";
	var contador = 0;    
	for (var i=0; i < rutCompleto.length; i++){
		u = rutCompleto.substring(i, i + 1);
		if (caracteres.indexOf(u) != -1)
		contador ++;
	}
	if ( contador==0 ) { return false }
	
	var rut = rutCompleto.substring(0,rutCompleto.length-1)
	var drut = rutCompleto.substring( rutCompleto.length-1 )
	var dvr = '0';
	var mul = 2;
	
	for (i= rut.length -1 ; i >= 0; i--) {
		suma = suma + rut.charAt(i) * mul
                if (mul == 7) 	mul = 2
		        else	mul++
	}
	res = suma % 11
	if (res==1)		dvr = 'k'
                else if (res==0) dvr = '0'
	else {
		dvi = 11-res
		dvr = dvi + ""
	}
	if ( dvr != drut.toLowerCase() ) { return false; }
	else { return true; }
}

function fecha(fechaNacimiento){
    var anioStr = fechaNacimiento.substring(6, fechaNacimiento.length);
    var anioInt = parseInt(anioStr);

    if (anioInt >= 2001) { return false; }
    
    return true;
}