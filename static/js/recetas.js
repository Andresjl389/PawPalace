const dirigir = document.getElementById("ir_receta");



dirigir.addEventListener("click", function() {
    window.location.href = '/info_receta/<int:receta_id>/';
});