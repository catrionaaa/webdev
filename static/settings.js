const blackCards = document.getElementById("black-cards");
const redCards = document.getElementById("red-cards");
const blueCards = document.getElementById("blue-cards");


// make the volume slider responsive
document.addEventListener("DOMContentLoaded", () => {
  const slider = document.getElementById("volume-slider");
  const volumeValue = document.getElementById("volume-value");

  slider.addEventListener("input", () => {
      volumeValue.textContent = slider.value + "%";
      localStorage.setItem("volume", slider.value / 100);
  });
});


// handles the user's card selection 
function selectCards(colour) {
  // fade out the other options depending on which cards were selected
  if (colour === "black") {
    blackCards.classList.remove("faded");
    redCards.classList.add("faded");
    blueCards.classList.add("faded");
  } else if (colour === "red") {
    blackCards.classList.add("faded");
    redCards.classList.remove("faded");
    blueCards.classList.add("faded");
  } else if (colour === "blue") {
    blackCards.classList.add("faded");
    redCards.classList.add("faded");
    blueCards.classList.remove("faded");
  }

  // save selection in localStorage
  localStorage.setItem("selectedCards", colour);
}


// add event listeners to each card option
blackCards.addEventListener("click", () => selectCards("black"));
redCards.addEventListener("click", () => selectCards("red"));
blueCards.addEventListener("click", () => selectCards("blue"));