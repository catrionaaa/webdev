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

//shuffle the deck, ID stored at localstorage/deckID
function shuffleDeck() {
  const shuffleDeckUrl = "https://deckofcardsapi.com/api/deck/"

  if(localStorage.getItem("deckID"))
    fetch(shuffleDeckUrl + localStorage.getItem("deckID") + "/shuffle")
      .then((res) => res.json())
      .then((data) => {
        if(data.success == false)
          fetchDeck();
      })
      .catch((err) => {
        console.error(err);
      })
  else
    fetchDeck();
}

//draw a single card from the deck and place it in a pile
function drawCard(pile) {
  const deckID = localStorage.getItem("deckID");

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/draw?count=1")
    .then(res => res.json())
    .then(data => {
      pileCard(pile, data.cards[0]);
      console.log(data.remaining);
      if(data.remaining < 1)
        shuffleDeck();
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

  render();
}

//draws a card from the deck into one of the piles
function draw(player) {
  console.log("player " + player + " draws");
  if(player == localStorage.getItem("turn")) {
    drawCard(player)
  } else
    console.log("Not your turn");
}

//this checks for the win condition
function snap(player) {
  if(localStorage.getItem("cardP0").charAt(0) == localStorage.getItem("cardP1").charAt(0))
    document.getElementById("announce").innerText = "Player " + (player + 1) + " wins!";
    localStorage.setItem("gameOver", true);
}

//determines which key was pressed upon keypress
function keyPress(key) {
  if(localStorage.getItem("gameOver") == "false") {
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
}

//this changes the html to reflect the state of the game
function render() {
  if(localStorage.getItem("cardP0"))
    document.getElementById("player0img").src="https://deckofcardsapi.com/static/img/" + localStorage.getItem("cardP0") + ".png";
  else
    document.getElementById("player0img").src="https://deckofcardsapi.com/static/img/back.png"
  
  if(localStorage.getItem("cardP1"))
    document.getElementById("player1img").src="https://deckofcardsapi.com/static/img/" + localStorage.getItem("cardP1") + ".png";
  else
    document.getElementById("player1img").src="https://deckofcardsapi.com/static/img/back.png"
}

//resets the game state to start a fresh game
function reset() {
  console.log("Resetting");

  localStorage.removeItem("cardP0");
  localStorage.removeItem("cardP1");

  localStorage.setItem("turn", 0);
  localStorage.setItem("gameOver", false);

  document.getElementById("announce").innerText = "";

  shuffleDeck();

  render();
}

document.addEventListener("keyup", e => keyPress(e.key));
document.getElementById("reset").addEventListener("click", reset);

reset();