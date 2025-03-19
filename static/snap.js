//initialises by checking localstorage for an existing game
function initialise() {
  if(!localStorage.getItem("deckId"))
    reset();
  else
    render();
}

//make a new deck, save the deckID to local storage and deal the cards evenly between two piles
function fetchDeck() {
  const newDeckUrl = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

  fetch(newDeckUrl)
    .then((res) => res.json())
    .then((data) => {
      console.log("Received deck")
      localStorage.setItem("deckID", data.deck_id);  
    })
    .catch((err) => {
      console.error(err);
    });
  
  localStorage.setItem("turn", 0);

}

//draw a single card from the deck and place it in a pile
function drawCard(pile) {
  const deckID = localStorage.getItem("deckID");

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/draw?count=1")
    .then(res => res.json())
    .then(data => {
      pileCard(pile, data.cards[0]);
    })
    .catch((err) => {
      console.error(err);
    })
  
  if(pile == 0)
    localStorage.setItem("turn", 1)
  else
    localStorage.setItem("turn", 0)
}

//place the drawn card on the top of the pile
function pileCard(pile, card) {
  localStorage.setItem("cardP" + pile, card.code);
}

//draws a card from the deck into one of the piles
function draw(player) {
  console.log("player " + player + " draws");
  if(player == localStorage.getItem("turn")) {
    drawCard(player)
  } else
    console.log("Not your turn");

  render();
}

//this checks for the win condition
function snap(player) {
  
}

//determines which key was pressed upon keypress
function keyPress(key) {
  switch(key) {
    case 'a': draw(0);
    break;
    case 'k': draw(1);
    break;
    case 'z': snap(0);
    break;
    case 'm': snap(1);
  }
}

//this changes the html to reflect the state of the game
function render() {
  if(localStorage.getItem("cardP0"))
    document.getElementById("player0").innerText = localStorage.getItem("cardP0")
  else 
    document.getElementById("player0").innerText = "EMPTY";

  if(localStorage.getItem("cardP1"))
    document.getElementById("player1").innerText = localStorage.getItem("cardP1")
  else
    document.getElementById("player1").innerText = "EMPTY";
}

function reset() {
  localStorage.removeItem("cardP0");
  localStorage.removeItem("cardP1");

  localStorage.setItem("turn", 0);

  fetchDeck();

  render;
}

document.addEventListener("keyup", e => keyPress(e.key));
document.getElementById("reset").addEventListener("click", reset())

initialise();