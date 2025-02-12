// JavaScript for toggling the sidebar
const toggleButton = document.getElementById("toggleButton");
const sidebar = document.getElementById("sidebar");
const content = document.getElementById("content");

toggleButton.addEventListener("click", () => {
  sidebar.classList.toggle("collapsed");
  content.classList.toggle("collapsed");
});
