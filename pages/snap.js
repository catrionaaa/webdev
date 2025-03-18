const pile1Name = pile1hW02fZCyu1
const pile2Name = pile2hCs9HGCBLP

function fetchDeck() {
  const deckUrl = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      console.log('Deck is ${data}')
      localStorage.setItem(deckID, data.deck_id);
    })
    .catch((err) => {
      console.error('error ${err}');
    });

  dealCards();
}

function dealCard() {
  deckID = localStorage.getItem(deckID);

  fetch("https://deckofcardsapi.com/api/deck/" + deckID + "/draw")
    .then(res => res.json())
    .then(data => (console.log('Drew ${data}')))
    .catch((err) => {
      console.error('error ${err}')
    })
}