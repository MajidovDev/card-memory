var cards = document.querySelectorAll('.card');

function trash(deleteButton) {
    var card = deleteButton.parentNode.parentNode;
    card.parentNode.removeChild(card);
  }

cards.forEach(function(card) {
  var menButtons = card.querySelectorAll('.men');
  var raqibButtons = card.querySelectorAll('.raqib');

  

  raqibButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      raqibButtons.forEach(function(btn) {
        btn.style.backgroundColor = 'red';
      });
      menButtons.forEach(function(btn) {
        btn.style.backgroundColor = '#2196f3';
      });
      button.style.backgroundColor = 'red'; // Only change the background color of the clicked button
    });
  });

  menButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      raqibButtons.forEach(function(btn) {
        btn.style.backgroundColor = '#2196f3';
      });
      menButtons.forEach(function(btn) {
        btn.style.backgroundColor = 'red';
      });
      button.style.backgroundColor = 'red'; // Only change the background color of the clicked button
    });
  });
});