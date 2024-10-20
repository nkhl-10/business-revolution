const categorySelect = document.getElementById("category");

categorySelect.addEventListener("change", function() {
  const selectedCategory = categorySelect.value;
  console.log("Selected category: " + selectedCategory);
});
