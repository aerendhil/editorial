$("#form_registro").validate({
    rules: {
        "txtCorreo":{
            required: true,
            email: true
        },
        "txtRun":{
            required: true,
            minlength: 9,
            maxlength: 10
        }
    },
    messages:{
        "txtCorreo":{
            required: "Ingrese su correo.",
            email: "El correo ingresado no cumple con el formato."
        },
        "txtRun":{
            required: "Ingrese su run",
            minlength: "El run ingresado es incorrecto",
            maxlength: "El run ingresado es incorrecto"
        }
    }
});