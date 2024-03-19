const menuSettings = document.getElementById("settings");
const settingsDiv = document.querySelector(".div_settings");
const container = document.querySelector(".container_div");

menuSettings.addEventListener("click", function() {
    settingsDiv.classList.toggle("active");
    container.classList.toggle("active");
});