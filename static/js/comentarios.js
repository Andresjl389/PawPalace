document.addEventListener("DOMContentLoaded", function() {
    var responseButtons = document.querySelectorAll("[id^='res_']");
    
    responseButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var coId = button.id.split('_')[1];
            var respuestaForo = document.getElementById("respuesta_"+coId)
            
            if (respuestaForo.style.display === "block") {
                respuestaForo.style.display = "none";  // Cerrar el formulario
            } else {
                // Cerrar todos los formularios antes de abrir el actual
                
                respuestaForo.style.display = "block";  // Abrir el formulario actual
            }


        });
    });
});
