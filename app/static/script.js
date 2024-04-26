const openButton = document.querySelector(" .open-button");
// const closeButton = document.querySelector(" .close-button")
const over = document.getElementById("over");
const modal = document.querySelector(" .main_box");

openButton.addEventListener("click", () => {
  openModal();
});

function openModal() {
  if (modal == null) return;
  modal.classList.add("active");
  over.classList.add("active");
}

over.addEventListener("click", () => {
  closeModal();
});

closeButton.addEventListener("click", () => {
  closeModal();
});

function closeModal() {
  if (modal == null) return;
  modal.classList.remove("active");
  over.classList.remove("active");
}
