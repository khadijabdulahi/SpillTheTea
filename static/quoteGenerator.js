document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("get-inspired")
    const quote = document.querySelector("blockquote p");
    const credit = document.querySelector("blockquote cite");
  
    async function newQuote() {
      const result = await fetch("https://api.quotable.io/random");
      const data = await result.json();
      if (result.ok) {
        quote.textContent = data.content;
        credit.textContent = data.author;
      } else {
        quote.textContent = "An error occured";
        console.log(data);
      }
    }
    button.addEventListener("click", newQuote);
      newQuote();
});
  