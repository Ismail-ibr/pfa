const openButton = document.querySelector(" .open-button");
const openButton2 = document.querySelector(" .open-button-2");
const openButtons3 = document.querySelectorAll(".open-button-3");
const openButtons4 = document.querySelectorAll(".open-button-4");

const over = document.getElementById("over");
const modal = document.querySelector(" .main_box");
const modal2 = document.querySelector(" .main_box2");
const modals3 = document.querySelectorAll(".main_box3");
const modals4 = document.querySelectorAll(".main_box4");

const button_close = document.getElementById("cancel");

openButtons3.forEach((button, index) => {
  button.addEventListener("click", () => {
    openModal(modals3[index]);
  });
});

openButtons4.forEach((button, index) => {
  button.addEventListener("click", () => {
    openModal(modals4[index]);
  });
});

openButton.addEventListener("click", () => {
  openModal(modal);
});

openButton2.addEventListener("click", () => {
  openModal(modal2);
});

function openModal(modalElement) {
  if (modalElement == null) return;
  modalElement.classList.add("active");
  over.classList.add("active");
}

over.addEventListener("click", () => {
  closeModal();
});

button_close.addEventListener("click", () => {
  closeModal();
});

closeButton.addEventListener("click", () => {
  closeModal();
});

function closeModal() {
  if (modal == null) return;
  modal.classList.remove("active");
  modal2.classList.remove("active");
  over.classList.remove("active");
  modals3.forEach((modal) => {
    modal.classList.remove("active");
  });
  modals4.forEach((modal) => {
    modal.classList.remove("active");
  });
}
