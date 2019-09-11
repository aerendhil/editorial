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
            required: true
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
            required: "Ingrese su fecha de nacimiento."
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

jQuery.validator.addMethod("validarRut", function(rutCompleto){
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
        return false;
    var tmp 	= rutCompleto.split('-');
    var digv	= tmp[1]; 
    var rut 	= tmp[0];
    if ( digv == 'K' ) digv = 'k' ;
    return (Fn.dv(rut) == digv );
});
