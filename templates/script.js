async function atualizarVagas() {
    const response = await fetch("/status");
    const data = await response.json()

    const listaCards = document.getElementById("cartoes");
    listaCards.innerHTML = "";

    for (const [numero, status] of Object.entries(data.vaga)) {
      const cardsDiv = document.createElement("div");
      cardsDiv.id = "cards";

      const card = document.createElement("div");
      card.className = "card " + (status === "Livre" ? "livre" : "ocupado");

      const titulo = document.createElement("h2");
      titulo.textContent = `Vaga ${numero}`;

      const paragrafo = document.createElement("p");
      paragrafo.textContent = `Status: ${status}`;

      card.appendChild(titulo);
      card.appendChild(paragrafo);
      cardsDiv.appendChild(card);
      listaCards.appendChild(cardsDiv);
    }
  }
  
  setInterval(atualizarVagas, 3000); // atualiza a cada 3 segundos
  atualizarVagas(); // chama na primeira vez