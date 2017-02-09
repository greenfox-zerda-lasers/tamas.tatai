var origList = document.querySelectorAll('li');
var myList = ['apple', 'banana', 'cat', 'dog'];

origList.forEach(function (item, index) {
  item.textContent = myList[index];
});
