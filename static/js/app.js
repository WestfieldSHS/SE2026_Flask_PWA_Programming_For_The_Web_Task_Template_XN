if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("/static/js/serviceworker.js")
            .then((res) => console.log("service worker registered"))
            .catch((err) => console.log("service worker not registered", err));
    });
}


// Simple Click-to-Jump A-Z Scrubber
document.addEventListener("DOMContentLoaded", () => {
  const alphaIndex = document.getElementById("alphaIndex");
  const cards = Array.from(document.querySelectorAll(".card[data-letter]"));
  if (!alphaIndex || cards.length === 0) return;

  // Gray out letters with no matching sharks
  const available = new Set(cards.map((c) => c.dataset.letter));
  alphaIndex.querySelectorAll(".alpha-letter").forEach((btn) => {
    if (!available.has(btn.dataset.target)) btn.classList.add("disabled");
  });

  // Scroll smoothly to the first shark starting with the clicked letter
  alphaIndex.addEventListener("click", (e) => {
    const btn = e.target.closest(".alpha-letter");
    if (!btn) return;

    const letter = btn.dataset.target;
    const targetCard =
      cards.find((c) => c.dataset.letter === letter) ||
      cards.find((c) => c.dataset.letter > letter);

    if (targetCard) {
      window.scrollTo({
        top: targetCard.getBoundingClientRect().top + window.scrollY - 90,
        behavior: "smooth",
      });
    }
  });
});