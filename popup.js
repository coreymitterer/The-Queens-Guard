document.getElementById("submit").addEventListener("click", function () {
    let count = document.getElementById("count").value;

    if (!count || isNaN(count) || count <= 0) {
        alert("Please enter a valid number!");
        return;
    }
    fetch(`http://localhost:5000/${count}`) // Replace with your local server URL
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json(); // or response.text() if the response is not JSON
    })
    .then(data => {
      console.log('Data received:', data);
      // Handle the data received from the server
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      // Handle errors during the fetch operation
    });
});