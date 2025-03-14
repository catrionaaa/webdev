let deckID;

function getFetch() {
	const url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1";

	fetch(url)
		.then((res) => res.json()) // parse response as JSON
		.then((data) => {
			console.log(`deck data is ${data}`);
			localStorage.setItem(deckID, data.deck_id);
		})
		.catch((err) => {
			console.log(`error ${err}`);
		});
	drawCard();
}

window.addEventListener("load", getFetch);