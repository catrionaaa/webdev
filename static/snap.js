const pile1Name = "pile1hW02fZCyu1"
const pile2Name = "pile2hCs9HGCBLP"

//make a new deck and save the deckID
function fetchDeck() {
  const newDeckUrl = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

  fetch(newDeckUrl)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      localStorage.setItem("deckID", data.deck_id);  
    })
    .catch((err) => {
      console.error(err);
    });

  console.log(localStorage.getItem("deckID"));

  dealCards();
}

//deal the entire deck from fetchDeck() into two piles
function dealCards() {

}

//draw a single card from the deck and place it in a pile
function dealCard() {
  const deckID = localStorage.getItem("deckID");

  console.log(deckID);

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/draw")
    .then(res => res.json())
    .then(data => {
      pileCard(data.cards[0]);
    })
    .catch((err) => {
      console.error(err);
    })
  
  console.log(card);
}

//place a single card into the pile provided
function pileCard(card) {

}

fetchDeck();