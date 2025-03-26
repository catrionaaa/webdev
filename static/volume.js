document.addEventListener("DOMContentLoaded", () => {
    const slider = document.getElementById("volume-slider");
    const volumeValue = document.getElementById("volume-value");
  
    slider.addEventListener("input", () => {
        volumeValue.textContent = slider.value + "%";
    });
});