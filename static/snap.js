//make a new deck, save the deckID to local storage and deal the cards evenly between two piles
function fetchDeck() {
  const newDeckUrl = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
  const pile1Name = "1"
  const pile2Name = "2"

  fetch(newDeckUrl)
    .then((res) => res.json())
    .then((data) => {
      console.log("Received deck")
      localStorage.setItem("deckID", data.deck_id);  
    })
    .catch((err) => {
      console.error(err);
    });

  dealCards(pile1Name, pile2Name);
}

//deal the entire deck from fetchDeck() into two piles
function dealCards(pile1, pile2) {
  for (let i = 0; i < 26; i++) {
    dealCard(pile1);
    dealCard(pile2);
  }

  const deckID = localStorage.getItem("deckID");
  
  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/pile/" + pile1 + "/list/")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch((err) => console.error(err));

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/pile/" + pile2 + "/list/")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch((err) => console.error(err));
  
}

//draw a single card from the deck and place it in a pile
function dealCard(pile) {
  const deckID = localStorage.getItem("deckID");

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/draw?count=1")
    .then(res => res.json())
    .then(data => {
      pileCard(pile, data.cards[0]);
    })
    .catch((err) => {
      console.error(err);
    })
}

//place a single card into the pile provided
function pileCard(pile, card) {
  const deckID = localStorage.getItem("deckID");

  console.log(card.code);

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/pile/" + pile + "/add/?cards=" + card.code)
    .catch((err) => {
      console.error(err);
    })
}

fetchDeck();