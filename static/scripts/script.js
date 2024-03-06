// script.js
document.addEventListener("DOMContentLoaded", function() {
  const projectLinks = document.querySelectorAll(".project a");

  projectLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      event.preventDefault();
      alert("This feature is not available yet.");
    });
  });
});
