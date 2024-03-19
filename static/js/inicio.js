// Obtén el botón y el div con la clase "options"
const menuIcon = document.getElementById("menu-icon");
const optionsDiv = document.querySelector(".options");
const listDiv = document.querySelector(".list");

// Función para desactivar el menú
function desactivarMenu() {
    optionsDiv.classList.remove("active");
    listDiv.classList.remove("active");
}

// Agrega un evento de clic al botón
menuIcon.addEventListener("click", function (event) {
    event.stopPropagation(); // Evitar que el clic se propague al documento
    // Toggle (agregar o quitar) la clase "active" en el div "options" y "list" para mostrar u ocultar
    optionsDiv.classList.toggle("active");
    listDiv.classList.toggle("active");
});

// Agrega un evento de clic al documento (cualquier parte de la página)
document.addEventListener("click", function (event) {
    // Verifica si el clic no ocurrió en el div "options" ni en el div "list"
    if (!optionsDiv.contains(event.target) && !listDiv.contains(event.target)) {
        // Si no se hizo clic en ninguno de los elementos, desactiva el menú
        desactivarMenu();
    }
});

// Agrega un evento de clic al cuerpo de la página para desactivar el menú si se hace clic en cualquier parte
document.body.addEventListener("click", desactivarMenu);


const menuSettings = document.getElementById("settings");
const settingsDiv = document.querySelector(".div_settings");
const container = document.querySelector(".container_div");

menuSettings.addEventListener("click", function() {
    settingsDiv.classList.toggle("active");
    container.classList.toggle("active");
});