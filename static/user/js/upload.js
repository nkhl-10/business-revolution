document.getElementById("ideas-form").addEventListener("submit", function(e) {
  e.preventDefault();

  var title = document.getElementById("title").value;
  var description = document.getElementById("description").value;
  var file = document.getElementById("file").files[0];
  var errorMessage = document.get
