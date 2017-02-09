// 1. Alert the content of the heading.
var headingContent = document.querySelector('h1');
alert(headingContent.innerHTML);

// 2. Write the content of the first paragraph to the console.
var firstParContent = document.querySelector('p');
console.log(firstParContent.innerHTML);

// 3. Alert the content of the second paragraph.
var secondParContent = document.querySelectorAll('p');
alert(secondParContent.innerHTML[1]);

// 4. Replace the heading's content with 'New content'.
var replaceHeading = document.querySelector('h1');
replaceHeading.innerHTML = 'New content';

// 5. Replace the last paragraph's content with the first paragraph's content.
var lastPar = document.getElementsByTagName('p');
lastPar[2].innerHTML = lastPar[0].innerHTML;
