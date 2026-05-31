// Initialize Toasts
const toastEl = document.getElementById("lushToast");
const toast = new bootstrap.Toast(toastEl, { delay: 1000 });

// Handle "Add to Bag" buttons
document.addEventListener("click", function (e) {
  if (
    e.target &&
    e.target.classList.contains("lush-btn-black") &&
    e.target.innerText.includes("ADD TO BAG")
  ) {
    e.preventDefault();
    toast.show();
  }
});
